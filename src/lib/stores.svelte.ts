function createHideNames() {	
    let hide_names = $state(false)

    function toggle() {
        hide_names = !hide_names
    }

    return {
        get hide_names() {
			return hide_names;
		},
        set hide_names(value) {
            hide_names = value;
        },
        toggle
    }
}

export const chn = createHideNames()

function animationSpeed(min: number, max: number) {
    let speed = $state(2000)


    return {
        get speed() {
            return speed;
        },
        set speed(value) {
            if (value < min) value = min
            if (value > max) value = max
            speed = value;
        },
        get_max() {
            return max
        },
        get_min() {
            return min
        }
    }
}

export const as = animationSpeed(100, 5000)