document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'es',
        events: [
            {
                title: 'Evento 1',
                start: '2024-07-01',
                end: '2024-07-02',
                description: 'Descripción del Evento 1',
                location: 'Lugar del Evento 1'
            },
            {
                title: 'Evento 2',
                start: '2024-07-05',
                description: 'Descripción del Evento 2',
                location: 'Lugar del Evento 2'
            }
            // Agrega más eventos aquí
        ],
        eventDidMount: function(info) {
            var tooltip = new Tooltip(info.el, {
                title: `<strong>${info.event.title}</strong><br>${info.event.extendedProps.description}<br>${info.event.extendedProps.location}`,
                html: true,
                placement: 'top',
                trigger: 'hover',
                container: 'body'
            });
        }
    });

    calendar.render();
});
