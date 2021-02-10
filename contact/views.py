from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
	if request.method == "POST":
		email = request.POST['contact_email']
		content = request.POST['contact_message']

		headers = {'reply-to': email}

		message = EmailMessage(
			'A visitor from your website has left a message!',
			content,
			email,
			['kennytran990518@gmail.com'],
			headers = headers,
		)

		message.send(fail_silently = False)

		return render(request, 'contact/contact.html', {'message': 'Message sent! I will get back to you ASAP.'})
	else:
		return render(request, 'contact/contact.html')