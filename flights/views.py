from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingDetailsSerializer, UpdateBookingSerializer, RegisterSerializer, UserSerializer,AdminSerializer


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	serializer_class = BookingSerializer
	def get_queryset(self):
		queryset = Booking.objects.filter(
			date__gte=datetime.today(),
			user=self.request.user

			)
		return queryset



class BookingDetails(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class UpdateBooking(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'
	def get_serializer_class(self):
		if self.request.user.is_staff:
			return AdminSerializer
		else:
			return UserSerializer


		# def get_permissions(self):
		#     if self.request == 'UpdateBooking':
		#         permission_classes = [IsAuthenticated]
		#     else:
		#         permission_classes = [IsUser]
		#     return [permission() for permission in permission_classes]
		# def check_object_permissions(self, request, obj):
		# 	if (obj.user == request.user):
		# 		return Booking.objects.filter(user=obj.id)
		# 	elif :
		# 		return Booking.objects.all()




class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class BookFlight(CreateAPIView):
	serializer_class = UpdateBookingSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, flight_id=self.kwargs['flight_id'])


class Register(CreateAPIView):
	serializer_class = RegisterSerializer
