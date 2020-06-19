from django.urls import path

from wm_test import views

app_name = 'wm_test'

urlpatterns = [

    path('', views.setting, name='setting'),
    path('add_sensor', views.add_sensor, name='add_sensor'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('manage_sensor', views.manage_sensor, name='manage_sensor'),

    path('live_report', views.live_report, name='live_report'),
    path('get_data_from_node_mcu', views.get_data_from_node_mcu, name='get_data_from_node_mcu'),
 #   path('show_sensor_graph', views.show_sensor_graph, name='show_sensor_graph'),
    path('show_sensor_graph', views.show_sensor_graph, name='show_sensor_graph'),
    path('fetch_sensor_values_ajax', views.fetch_sensor_values_ajax, name='fetch_sensor_values_ajax'),
 #   path('fetch_sensor_values_ajax', views.fetch_sensor_values_ajax, name='fetch_sensor_values_ajax'),
 #   path('fetch_sensor_comman_values_ajax', views.fetch_sensor_comman_values_ajax, name='fetch_sensor_comman_values_ajax'),
 #   path('fetch_sensor_values_ajax_CO', views.fetch_sensor_values_ajax_CO, name='fetch_sensor_values_ajax_CO'),
 #   path('live_data_graph', views.live_data_graph, name='live_data_graph'),
 #   path('fetch_sensor_values_all_ajax', views.fetch_sensor_values_all_ajax, name='fetch_sensor_values_all_ajax'),
 #   path('sensor_data', views.sensor_data, name='sensor_data'),
    path('start_save_sensor', views.start_save_sensor, name='start_save_sensor'),
    path('run_back_save', views.run_back_save, name='run_back_save'),

    path('wind_hourly_report', views.wind_hourly_report, name='wind_hourly_report'),
    path('fetch_wind_hourly_report_ajax', views.fetch_wind_hourly_report_ajax, name='fetch_wind_hourly_report_ajax'),

    path('frequency_distribution_count_report', views.frequency_distribution_count_report, name='frequency_distribution_count_report'),
    path('fetch_frequency_distribution_count_ajax', views.fetch_frequency_distribution_count_ajax, name='fetch_frequency_distribution_count_ajax'),

    path('frequency_distribution_normalized_report', views.frequency_distribution_normalized_report,name='frequency_distribution_normalized_report'),
    path('fetch_frequency_distribution_normalized_ajax', views.fetch_frequency_distribution_normalized_ajax,name='fetch_frequency_distribution_normalized_ajax'),

    path('show_frequency_distribution_reportnormalised_bar_graph', views.show_frequency_distribution_reportnormalised_bar_graph,name='show_frequency_distribution_reportnormalised_bar_graph'),
    path('fetch_show_frequency_distribution_reportnormalised_bar_graph_ajax', views.fetch_show_frequency_distribution_reportnormalised_bar_graph_ajax,name='fetch_show_frequency_distribution_reportnormalised_bar_graph_ajax'),

    path('show_windrose_diagram', views.show_windrose_diagram, name='show_windrose_diagram'),
    path('fetch_show_windrose_diagram_ajax', views.fetch_show_windrose_diagram_ajax, name='fetch_show_windrose_diagram_ajax'),

    path('sensor_hourly_report', views.sensor_hourly_report, name='sensor_hourly_report'),
    path('fetch_sensor_hourly_report_ajax', views.fetch_sensor_hourly_report_ajax, name='fetch_sensor_hourly_report_ajax'),
    path('fetch_show_sensor_hourly_report_graph_ajax', views.fetch_show_sensor_hourly_report_graph_ajax, name='fetch_show_sensor_hourly_report_graph_ajax'),
    path('show_sensor_hourly_report_graph', views.show_sensor_hourly_report_graph, name='show_sensor_hourly_report_graph'),

    path('hour_duration_avg_report', views.hour_duration_avg_report, name='hour_duration_avg_report'),
    path('fetch_hour_duration_avg_report_ajax', views.fetch_hour_duration_avg_report_ajax, name='fetch_hour_duration_avg_report_ajax'),
    path('show_hour_duration_avg_report_graph', views.show_hour_duration_avg_report_graph, name='show_hour_duration_avg_report_graph'),
    path('fetch_show_hour_duration_avg_report_graph_ajax', views.fetch_show_hour_duration_avg_report_graph_ajax, name='fetch_show_hour_duration_avg_report_graph_ajax'),

    path('date_and_hour_duration_avg_report', views.date_and_hour_duration_avg_report, name='date_and_hour_duration_avg_report'),
    path('fetch_date_and_hour_duration_avg_report_ajax', views.fetch_date_and_hour_duration_avg_report_ajax, name='fetch_date_and_hour_duration_avg_report_ajax'),
    path('show_date_and_hour_duration_avg_report_graph', views.show_date_and_hour_duration_avg_report_graph, name='show_date_and_hour_duration_avg_report_graph'),
    path('fetch_show_date_and_hour_duration_avg_report_graph_ajax', views.fetch_show_date_and_hour_duration_avg_report_graph_ajax, name='fetch_show_date_and_hour_duration_avg_report_graph_ajax'),
 
]    
