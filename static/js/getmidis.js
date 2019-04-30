$(document).ready(function() {
    $.ajax({
        url: 'http://0.0.0.0:8080/getMIDIs',
        success: function(response) {
            var parsed = JSON.parse(response.items);
            for (var i = 0; i < parsed.length; i++) {
                // add each MIDI file as a button, pass song name to next page
                $('#midifiles').append(
                    '<input type="submit" class="btn btn-link" name="song_name" value="' + parsed[i] + '"><br>');
            }
        },
        error: function(error) {
            console.log(error);
        }
    });
});
