 $(document).ready(function () {
        $('#add_click').click(function () {
            $.post(
                '/api/v1/clicks',
                null,
                function (status) {
                    console.log(status);
                    $('#clicks').text(function(){
                        return "Clicks: "+status.amount;
                    });
                }
            );

        });

        $('#get_clicks').click(function () {
            $.get(
                '/api/v1/clicks',
                null,
                function (status) {
                    console.log(status);
                }
            )
        });

        $('#del_click').click(function () {
            $.ajax({
                url: '/api/v1/clicks',
                type: 'DELETE',
                success: function (status) {
                    console.log(status);
                     $('#clicks').text(function(){
                        return "Clicks: "+status.amount;
                    });
                }
            });

        });

        $('#send_name').click(function(){
            $.post(
                '/api/v1/users',
                {"name" : $('#name_input').val()},
                function (status) {
                    console.log(status);
                    $('#name_par').text(function(){
                        return "Name: "+status.name;
                    });
                }
            )
        })
 });