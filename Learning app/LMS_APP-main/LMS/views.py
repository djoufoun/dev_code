from django.shortcuts import render, redirect, get_object_or_404
from lmsapp.models import Categories, Course, Level, Video, UserCourse, Payment
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages
from . settings import *
import razorpay
from time import time
from django.views.decorators.csrf import csrf_exempt



client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

def BASE(request):
    return render(request, 'base.html')

def PAGE_NOT_FOUND(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category': category,
    }
    return render(request, 'error/404.html', context)

def HOME(request):
    category = Categories.objects.all().order_by('id')
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    
    context = {
        'category': category,
        'course': course,
    }
    return render(request, 'main/home.html', context)

def SINGLECOURSE(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    FreeCourse_count = Course.objects.filter(price = 0).count()
    PaidCourse_count = Course.objects.filter(price__gte=1).count()
    context = {
        'category': category,
        'level' : level,
        'course' : course,
        'FreeCourse_count' : FreeCourse_count,
        'PaidCourse_count' : PaidCourse_count,
    }

    return render(request, 'main/singlecourse.html', context)

def filter_data(request):
    categories = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')

    if price == ['PriceFree']:
       course = Course.objects.filter(price=0)
    elif price == ['PricePaid']:
       course = Course.objects.filter(price__gte=1)
    elif price == ['PriceAll']:
       course = Course.objects.all()
    elif categories:
       course = Course.objects.filter(category__id__in=categories).order_by('-id')
    elif level:
       course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
       course = Course.objects.all().order_by('-id')

    context = {
        'course': course
    }

    t = render_to_string('ajax/course.html', context)

    return JsonResponse({'data': t})

def ABOUTUS(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category': category,
    }
    return render(request, 'main/aboutus.html', context)

def CONTACTUS(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category': category,
    }

    return render(request, 'main/contactus.html', context)


def SEARCH_COURSE(request):
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    category = Categories.get_all_category(Categories)
    context = {
        'course':course,
        'category': category,
    }
    return render(request,'search/search.html',context)

def COURSE_DETAIL(request, slug):
    course = Course.objects.filter(slug= slug)
    time_duration = Video.objects.filter(course__slug = slug).aggregate(sum=Sum('time_duration'))
    category = Categories.get_all_category(Categories)

    course_id = Course.objects.get(slug=slug)
    try:
        check_enroll = UserCourse.objects.get(user=request.user, course=course_id)
    except UserCourse.DoesNotExist:
        check_enroll = None
    
    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    
    context ={
        'course': course,
        'category': category,
        'time_duration': time_duration,
        'check_enroll': check_enroll,
    }

    return render(request, 'course/course_detail.html', context)

def CHECKOUT(request, slug):
    course = Course.objects.get(slug = slug)
    action = request.GET.get('action')
    order = None
    if course.price == 0:
        course = UserCourse(
            user = request.user,
            course = course
        )
        course.save()
        messages.success(request, 'Course Is Successfully Enrolled!')
        return redirect('my_course')
    elif action == 'create_payment':
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            country = request.POST.get('country')
            address_1 = request.POST.get('address_1')
            address_2 = request.POST.get('address_2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            postcode = request.POST.get('postcode')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            order_comments = request.POST.get('order_comments')

            amount_cal = course.price -(course.price * course.discount /100)
            amount = int(amount_cal) * 100
            currency = "INR"
            notes  = {
                'name': f'{first_name} {last_name}',
                'country': country,
                'address': f'{address_1} {address_2}',
                'city': city,
                'state': state,
                'postcode': postcode,
                'email': email,
                'phone': phone,
                'order_comments': order_comments,
            }
            receipt = f"Ashu-{int (time())}"
            order = client.order.create(
                {
                'receipt': receipt,
                'notes': notes,
                'amount': amount,
                'currency': currency,
                }
            )
            payment = Payment(
                course= course,
                user = request.user,
                order_id = order.get('id')
            )
            payment.save()
    context = { 
        'course': course,
        'order': order,
    }

    return render(request, 'checkout/checkout.html', context)


def MY_COURSE(request):
    category = Categories.get_all_category(Categories)
    course = UserCourse.objects.filter(user = request.user)
    context = { 
        'course': course,
        'category': category,
    }
    return render(request, 'course/my_course.html', context)

@csrf_exempt
def VERIFY_PAYMENT(request):
    if request.method == "POST":
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            usercourse = UserCourse(
                user = payment.user,
                course = payment.course,
            )
            usercourse.save()
            payment.user_course = usercourse
            payment.save()

            context = {
                'data': data,
                'payment': payment,
            }
            return render(request, 'verify_payment/success.html', context)
        except:
            return render(request, 'verify_payment/fail.html')

def WATCH_COURSE(request, slug):
    lecture = request.GET.get('lecture')
    course_id = Course.objects.get(slug=slug)
    course = Course.objects.filter(slug=slug)
    try:
        check_enroll = UserCourse.objects.get(user=request.user, course=course_id)
        video = Video.objects.get(id=lecture)
        if course.exists():
            course = course.first()
        else:
            return redirect("404")
    except UserCourse.DoesNotExist:
        return redirect('404')
    context = {
        'course': course,
        'video': video,
        'lecture': lecture,
    }
    return render(request, 'course/watch_course.html', context)

# def WATCH_COURSE(request, slug):
#     lecture = request.GET.get('lecture')
#     course_id = Course.objects.get(slug=slug)
#     course = Course.objects.filter(slug=slug)
#     if course.exists():
#             course = course.first()
#     else:
#             return redirect("404")
#     context = {
#         'course': course,
#     }
#     return render(request, 'course/watch_course.html', context)