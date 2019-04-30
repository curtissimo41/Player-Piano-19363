$(document).ready(function() {
    $.ajax({
        url: 'http://0.0.0.0:8080/playsong/get_song_info',
        success: function(response) {
            var parsed = JSON.parse(response.items);

            var track_dict = parsed['track_dict']

            $('#BPM-field').val(parsed['BPM']);
            $('#songEndTime').html(parsed['length_disp']);
            $('#time-slider').attr('data-slider-max', parsed['length']);
            for (var i = 0; i < Object.keys(track_dict).length; i++) {
                $('#tracks-checkboxes').append('<input type="checkbox" checked \
                value = "' + track_dict[i][0] + '"> ' + track_dict[i][0] +
                ' (Note Count: ' + track_dict[i][1] + ') <br>')
            }
        },
        error: function(error) {
            console.log(error);
        }
    });

    // function to play song when play button is hit
    $("#play").click(function() {
        $.ajax({
            url: "http://0.0.0.0:8080/playsong/play",
            success: function(response) {
                // stuff
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    // function to pause song when pause button is hit
    $("#pause").click(function() {
        $.ajax({
            url: "http://0.0.0.0:8080/playsong/pause",
            success: function(response) {
                // stuff
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    // function to stop song when stop button is hit
    $("#stop").click(function() {
        $.ajax({
            url: "http://0.0.0.0:8080/playsong/stop",
            success: function(response) {
                // stuff
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

});
