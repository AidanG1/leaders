export function createHideNames() {	
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