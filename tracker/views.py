from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Sum
from django.http import JsonResponse
from django.middleware.csrf import get_token
from .models import WeeklyDelivery

class DeliveryListView(ListView):
    model = WeeklyDelivery
    template_name = 'tracker/delivery_list.html'
    context_object_name = 'deliveries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        totals = WeeklyDelivery.objects.aggregate(
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
        return context

class DeliveryCreateView(CreateView):
    model = WeeklyDelivery
    template_name = 'tracker/delivery_form.html'
    fields = '__all__'
    success_url = reverse_lazy('delivery_list')

    def get_initial(self):
        initial = super().get_initial()
        previous_delivery = WeeklyDelivery.objects.order_by('-start_date', '-pk').first()

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

    def form_valid(self, form):
        super().form_valid(form)
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return super().form_valid(form)

class DeliveryUpdateView(UpdateView):
    model = WeeklyDelivery
    template_name = 'tracker/delivery_form.html'
    fields = ['start_date', 'end_date', 'video_drive_target', 'video_drive_achieved', 'video_drive_shortfall', 'travel_mobile_target', 'travel_mobile_achieved', 'travel_mobile_shortfall', 'mca_sourcing_target', 'mca_sourcing_achieved', 'mca_sourcing_shortfall', 'total_target', 'total_achieved', 'total_shortfall']
    success_url = reverse_lazy('delivery_list')

    def get_template_names(self):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return ['tracker/delivery_form_modal.html']
        return super().get_template_names()

    def form_valid(self, form):
        super().form_valid(form)
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return super().form_valid(form)

class DeliveryDeleteView(DeleteView):
    model = WeeklyDelivery
    template_name = 'tracker/delivery_confirm_delete.html'
    success_url = reverse_lazy('delivery_list')

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return super().delete(request, *args, **kwargs)
