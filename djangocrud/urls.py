"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views
from home import viewsh
from primerpaso import viewsp1
from segundopaso import viewsp2
from tercerpaso import viewsp3
from cuartopaso import viewsp4
from quintopaso import viewsp5
from sextopaso import viewsp6
from septimopaso import viewsp7

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', viewsh.home, name='home'),
    path('aboutprogram/',viewsh.aboutprogram, name='aboutprogram'),
    path('tutor/',viewsh.tutor, name='tutor'),
    path('areas_profesionales/',viewsh.areas_profesionales, name='areas_profesionales'),
    path('directorio_universidades/',viewsh.directorio_universidades, name='directorio_universidades'),
    path('becas_vigentes/',viewsh.becas_vigentes, name='becas_vigentes'),

    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('permission-denied/', views.permissiondenied, name='permission_denied'),
    path('homeadmin/', views.homeadmin, name='homeadmin'),
    path('homeuser/', views.homeuser, name='homeuser'),
    path('final/', views.final, name='final'),

    path('primerpaso/',viewsp1.primerpaso, name='primerpaso'),
    path('imagen-primer-paso/',viewsp1.imagen_primerpaso, name='imagen-primer-paso'),
    path('presentacion-primer-paso/',viewsp1.presentacion_primerpaso, name='presentacion-primer-paso'),
    path('video-primer-paso/',viewsp1.video_primerpaso, name='video-primer-paso'),
    path('formato-primer-paso/',viewsp1.formato_primerpaso, name='formato-primer-paso'),
    path('mis-intereses-s2/',viewsp1.primerpasos2, name='mis-intereses-s2'),
    path('infografia-primer-paso/',viewsp1.infografia_primerpaso, name='infografia-primer-paso'),
    path('instrucciones-primer-paso/',viewsp1.instrucciones_primerpaso, name='instrucciones-primer-paso'),
    path('test-primer-paso/',viewsp1.test_primerpaso, name='test-primer-paso'),
    path('resultados-primer-paso/',viewsp1.resultados_primerpaso, name='resultados-primer-paso'),
    path('interactiva/', viewsp1.presentacion_interactiva, name='presentacion-interactiva'),
    path('update-progress/', viewsp1.update_progress, name='update-progress'),
    
    path('segundopaso/',viewsp2.segundopaso,name='segundopaso'),
    path('frase-segundo-paso/',viewsp2.frase_segundopaso,name='frase-segundo-paso'),
    path('presentacion-segundo-paso/',viewsp2.presentacion_segundopaso,name='presentacion-segundo-paso'),
    path('instrucciones-segundo-paso/',viewsp2.instrucciones_segundopaso, name='instrucciones-segundo-paso'),
    path('test-segundo-paso/',viewsp2.test_segundopaso, name='test-segundo-paso'),
    path('resultados-segundo-paso',viewsp2.resultados_segundopaso, name='resultados-segundo-paso'),

    path('tercerpaso/',viewsp3.tercerpaso, name='tercer-paso'),
    path('infografia-tercer-paso/',viewsp3.infografia_tercerpaso, name='infografia-tercer-paso'),
    path('mi-entorno-s2/',viewsp3.mi_entorno_s2, name='mi-entorno-s2'),
    path('tablero-interactivo-tercer-paso/',viewsp3.tablero_tercerpaso, name='tablero-interactivo-tercer-paso'),
    path('video-tercer-paso/',viewsp3.video_tercerpaso, name='video-tercer-paso'),
    path('mi-entorno-s3/',viewsp3.mi_entorno_s3, name='mi-entorno-s3'),
    path('video-consejo-tercer-paso/',viewsp3.video_consejo_tercerpaso, name='video-consejo-tercer-paso'),
    path('mi-entorno-s4/',viewsp3.mi_entorno_s4, name='mi-entorno-s4'),
    path('presentacion-tercerpaso/', viewsp3.presentacion_tercerpaso, name='presentacion-interactiva-tercer-paso'),

    path('cuartopaso/',viewsp4.cuartopaso, name='cuartopaso'),
    path('tablero-cuarto-paso/',viewsp4.tablero_cuartopaso, name='tablero-cuarto-paso'),
    path('video-cuarto-paso/',viewsp4.video_cuartopaso, name='video-cuarto-paso'),
    path('agenda-cuarto-paso/',viewsp4.agenda_cuartopaso, name='agenda-cuarto-paso'),

    path('quintopaso/', viewsp5.quintopaso, name='quintopaso'),
    path('imagen-quinto-paso/', viewsp5.imagen_quintopaso, name='imagen-quinto-paso'),
    path('tablero-quinto-paso/', viewsp5.tablero_quintopaso, name='tablero-quinto-paso'),
    path('infografia-quinto-paso/', viewsp5.infografia_quintopaso, name='infografia-quinto-paso'),


    path('sextopaso/', viewsp6.sextopaso, name='sextopaso'),
    path('tablero-sextopaso/', viewsp6.tablero_sextopaso, name='tablero-sextopaso'),

    path('septimopaso/', viewsp7.septimopaso, name='septimopaso'),
    path('frase-septimo-paso/', viewsp7.frase_septimopaso, name='frase-septimo-paso'),
    path('imagen-septimo-paso/', viewsp7.imagen_septimopaso, name='imagen-septimo-paso'),
    path('video-septimo-paso/', viewsp7.video_septimopaso, name='video-septimo-paso'),
    path('mi-plan-s2/', viewsp7.mi_plan_s2, name='mi-plan-s2'),
    path('infografia-septimo-paso/', viewsp7.infografia_septimopaso, name='infografia-septimo-paso'),
    path('imagen2-septimo-paso/', viewsp7.imagen2_septimopaso, name='imagen2-septimo-paso'),
    path('formato-septimo-paso/', viewsp7.formato_septimopaso, name='formato-septimo-paso'),
    path('formato2-septimo-paso/', viewsp7.formato2_septimopaso, name='formato2-septimo-paso'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset_form.html',
        email_template_name='password_reset_email.txt',
        subject_template_name='password_reset_subject.txt',
    ), name='password_reset'),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
    
]
