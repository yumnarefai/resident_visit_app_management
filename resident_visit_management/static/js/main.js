"""
$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        var url = $(this).attr('action');
        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            success: function(response) {
                alert(response.message);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('#search_visit').on('click', function() {
        var visitor = $('#visitor').val();
        $.ajax({
            type: 'GET',
            url: '/search_visit',
            data: { visitor: visitor },
            success: function(response) {
                var visits = response;
                var html = '';
                for (var i = 0; i < visits.length; i++) {
                    html += '<p>Visit ID: ' + visits[i].id + ', Scheduled Time: ' + visits[i].scheduled_time + ', Is Approved: ' + visits[i].is_approved + ', Resident: ' + visits[i].resident + ', Visitor: ' + visits[i].visitor + '</p>';
                }
                $('#search_results').html(html);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
"""
