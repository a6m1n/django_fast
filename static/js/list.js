    var favorite = [];

    $('#select-all').click(function(event) {
        if(this.checked) {
            $(':checkbox').each(function() {
                this.checked = true;
                favorite.push($(this).attr("name"));
            });
        } else {
            $(':checkbox').each(function() {
                favorite.splice($(this).attr("name"));
                this.checked = false;
            });

        }
    });

    $('.check').click(function(event) {
        if(this.checked) {
            favorite.push($(this).attr("name"));
        } else {
            const index = favorite.indexOf($(this).attr("name"));
            favorite.splice(index, 1);
        }
    });

    $('.delete_one').click(function(event) {
        document.getElementById($(this).attr("name")).checked = true;
        document.getElementById('forms').submit();
});