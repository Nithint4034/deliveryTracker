from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import JsonResponse
from django.middleware.csrf import get_token

from .models import WeeklyDelivery, WeeklyDeliverySecondary, ClientDeliveryStatus


@login_required
def home(request):
    return render(request, 'tracker/home.html')


class DeliveryTrackerContextMixin:
    tracker_title = 'Weekly Internal Delivery'
    page_subtitle = 'Track weekly targets, achievements, and shortfalls in one dashboard.'
    create_url_name = 'delivery_create'
    update_url_name = 'delivery_update'
    delete_url_name = 'delivery_delete'
    cancel_url_name = 'delivery_list'

    def get_tracker_context(self):
        return {
            'tracker_title': self.tracker_title,
            'page_subtitle': self.page_subtitle,
            'create_url_name': self.create_url_name,
            'update_url_name': self.update_url_name,
            'delete_url_name': self.delete_url_name,
            'cancel_url_name': self.cancel_url_name,
        }


class BaseDeliveryListView(LoginRequiredMixin, DeliveryTrackerContextMixin, ListView):
    template_name = 'tracker/delivery_list.html'
    context_object_name = 'deliveries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        totals = self.model.objects.aggregate(
            video_drive_target=Sum('video_drive_target'),
            video_drive_achieved=Sum('video_drive_achieved'),
            video_drive_shortfall=Sum('video_drive_shortfall'),
            travel_mobile_target=Sum('travel_mobile_target'),
            travel_mobile_achieved=Sum('travel_mobile_achieved'),
            travel_mobile_shortfall=Sum('travel_mobile_shortfall'),
            mca_sourcing_target=Sum('mca_sourcing_target'),
            mca_sourcing_achieved=Sum('mca_sourcing_achieved'),
            mca_sourcing_shortfall=Sum('mca_sourcing_shortfall'),
            total_target=Sum('total_target'),
            total_achieved=Sum('total_achieved'),
            total_shortfall=Sum('total_shortfall'),
        )
        context['totals'] = totals
        context['csrf_token'] = get_token(self.request)
        context.update(self.get_tracker_context())
        return context


class BaseDeliveryCreateView(LoginRequiredMixin, DeliveryTrackerContextMixin, CreateView):
    template_name = 'tracker/delivery_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy(self.cancel_url_name)

    def get_initial(self):
        initial = super().get_initial()
        previous_delivery = self.model.objects.order_by('-start_date', '-pk').first()

        if previous_delivery is not None:
            initial.update({
                'video_drive_target': previous_delivery.video_drive_target,
                'travel_mobile_target': previous_delivery.travel_mobile_target,
                'mca_sourcing_target': previous_delivery.mca_sourcing_target,
            })

        return initial

    def get_template_names(self):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return ['tracker/delivery_form_modal.html']
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_tracker_context())
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return response


class BaseDeliveryUpdateView(LoginRequiredMixin, DeliveryTrackerContextMixin, UpdateView):
    template_name = 'tracker/delivery_form.html'
    fields = ['start_date', 'end_date', 'video_drive_target', 'video_drive_achieved', 'video_drive_shortfall', 'travel_mobile_target', 'travel_mobile_achieved', 'travel_mobile_shortfall', 'mca_sourcing_target', 'mca_sourcing_achieved', 'mca_sourcing_shortfall', 'total_target', 'total_achieved', 'total_shortfall']

    def get_success_url(self):
        return reverse_lazy(self.cancel_url_name)

    def get_template_names(self):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return ['tracker/delivery_form_modal.html']
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_tracker_context())
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return response


class BaseDeliveryDeleteView(LoginRequiredMixin, DeliveryTrackerContextMixin, DeleteView):
    template_name = 'tracker/delivery_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(self.cancel_url_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_tracker_context())
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return response


class DeliveryListView(BaseDeliveryListView):
    model = WeeklyDelivery


class DeliveryCreateView(BaseDeliveryCreateView):
    model = WeeklyDelivery


class DeliveryUpdateView(BaseDeliveryUpdateView):
    model = WeeklyDelivery


class DeliveryDeleteView(BaseDeliveryDeleteView):
    model = WeeklyDelivery


class SecondaryDeliveryListView(BaseDeliveryListView):
    model = WeeklyDeliverySecondary
    tracker_title = 'Weekly Internal Delivery - Mexico'
    create_url_name = 'secondary_delivery_create'
    update_url_name = 'secondary_delivery_update'
    delete_url_name = 'secondary_delivery_delete'
    cancel_url_name = 'secondary_delivery_list'


class SecondaryDeliveryCreateView(BaseDeliveryCreateView):
    model = WeeklyDeliverySecondary
    tracker_title = 'Weekly Internal Delivery - Mexico'
    create_url_name = 'secondary_delivery_create'
    update_url_name = 'secondary_delivery_update'
    delete_url_name = 'secondary_delivery_delete'
    cancel_url_name = 'secondary_delivery_list'


class SecondaryDeliveryUpdateView(BaseDeliveryUpdateView):
    model = WeeklyDeliverySecondary
    tracker_title = 'Weekly Internal Delivery - Mexico'
    create_url_name = 'secondary_delivery_create'
    update_url_name = 'secondary_delivery_update'
    delete_url_name = 'secondary_delivery_delete'
    cancel_url_name = 'secondary_delivery_list'


class SecondaryDeliveryDeleteView(BaseDeliveryDeleteView):
    model = WeeklyDeliverySecondary
    tracker_title = 'Weekly Internal Delivery - Mexico'
    create_url_name = 'secondary_delivery_create'
    update_url_name = 'secondary_delivery_update'
    delete_url_name = 'secondary_delivery_delete'
    cancel_url_name = 'secondary_delivery_list'


# Client Delivery Status Views
class ClientDeliveryContextMixin:
    tracker_title = 'Client Delivery Status - Mexico'
    page_subtitle = 'Track deliveries by phase with client inventory status.'
    create_url_name = 'client_delivery_create'
    update_url_name = 'client_delivery_update'
    delete_url_name = 'client_delivery_delete'
    cancel_url_name = 'client_delivery_list'

    def get_tracker_context(self):
        return {
            'tracker_title': self.tracker_title,
            'page_subtitle': self.page_subtitle,
            'create_url_name': self.create_url_name,
            'update_url_name': self.update_url_name,
            'delete_url_name': self.delete_url_name,
            'cancel_url_name': self.cancel_url_name,
        }


class ClientDeliveryListView(LoginRequiredMixin, ClientDeliveryContextMixin, ListView):
    model = ClientDeliveryStatus
    template_name = 'tracker/client_delivery_list.html'
    context_object_name = 'deliveries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        totals = ClientDeliveryStatus.objects.aggregate(
            planned_delivery_count=Sum('planned_delivery_count'),
            actual_delivery_count=Sum('actual_delivery_count'),
            total_new_poi_delivery_till_date=Sum('total_new_poi_delivery_till_date'),
            new_poi_inventory_not_delivered=Sum('new_poi_inventory_not_delivered'),
        )
        context['totals'] = totals
        context['csrf_token'] = get_token(self.request)
        context.update(self.get_tracker_context())
        return context


class ClientDeliveryCreateView(LoginRequiredMixin, ClientDeliveryContextMixin, CreateView):
    model = ClientDeliveryStatus
    template_name = 'tracker/client_delivery_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy(self.cancel_url_name)

    def get_template_names(self):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return ['tracker/client_delivery_form_modal.html']
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_tracker_context())
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return response


class ClientDeliveryUpdateView(LoginRequiredMixin, ClientDeliveryContextMixin, UpdateView):
    model = ClientDeliveryStatus
    template_name = 'tracker/client_delivery_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy(self.cancel_url_name)

    def get_template_names(self):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return ['tracker/client_delivery_form_modal.html']
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_tracker_context())
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return response


class ClientDeliveryDeleteView(LoginRequiredMixin, ClientDeliveryContextMixin, DeleteView):
    model = ClientDeliveryStatus
    template_name = 'tracker/client_delivery_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(self.cancel_url_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_tracker_context())
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return response
