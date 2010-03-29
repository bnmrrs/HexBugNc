var hexbug = {

    walk_state: {
        'forward': false,
        'reverse': false
    },
    spin_state: {
        'right': false,
        'left': false
    },

    walk_timer: false,
    spin_timer: false,

    forward: function()
    {
        if (!hexbug.walk_state.forward) {
            hexbug.walk_state.reverse = false;
            hexbug.walk_state.forward = true;

            hexbug.send_cmd('forward');
        }

        hexbug.extend_walk_timeout();
    },

    reverse: function()
    {
        if (!hexbug.walk_state.reverse) {
          hexbug.walk_state.forward = false;
          hexbug.walk_state.reverse = true;

          hexbug.send_cmd('reverse');
        }

        hexbug.extend_walk_timeout();
    },

    right: function()
    {
        if (!hexbug.spin_state.right) {
            hexbug.spin_state.left = false;
            hexbug.spin_state.right = true;

            hexbug.send_cmd('right');
        }

        hexbug.extend_spin_timeout();
    },

    left: function()
    {
        if (!hexbug.spin_state.left) {
            hexbug.spin_state.right = false;
            hexbug.spin_state.left = true;

            hexbug.send_cmd('left');
        }

        hexbug.extend_spin_timeout();
    },

    extend_walk_timeout: function()
    {
        if (hexbug.walk_timer) {
            clearTimeout(hexbug.walk_timer);
            hexbug.walk_timer = false;
        }

        hexbug.walk_timer = setTimeout(function() {
            hexbug.send_cmd('stop_walk');

            hexbug.walk_state.forward = false;
            hexbug.walk_state.reverse = false;
        }, 100);
    },

    extend_spin_timeout: function()
    {
        if (hexbug.spin_timer) {
            clearTimeout(hexbug.spin_timer);
            hexbug.spin_timer = false;
        }

        hexbug.spin_timer = setTimeout(function() {
            hexbug.send_cmd('stop_spin');

            hexbug.spin_state.right = false;
            hexbug.spin_state.left = false;
        }, 100);
    },

    send_cmd: function(cmd)
    {
        $.post('/send_command', cmd);
    }
};
