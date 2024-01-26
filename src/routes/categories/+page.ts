import { supabase } from "$lib/db";

export const load = async () => {
    const { data, error } = await supabase.from('categories').select('*')

    if (error) {
        console.log(error)
    }

    let categories = data

    if (!categories) categories = []
 
	return {
		categories,
	};
};