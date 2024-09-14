export let apiUrl;

if (import.meta.env.VITE_API_URL) {
	apiUrl = import.meta.env.VITE_API_URL;
} else {
	apiUrl = import.meta.env.DEV ? 'http://localhost:3000' : '/api';
}

export async function getAllData() {
	const views = ['quarter', 'hours', 'year'];

	let overview = {};
	let components = [];
	let componentsData = {};

	let response;

	response = await fetch(apiUrl + `/overview/`);
	overview = await response.json();

	response = await fetch(apiUrl + `/components/`);
	components = await response.json();

	for (const c of components) {
		componentsData[c] = {};

		for (const v of views) {
			response = await fetch(apiUrl + `/components/?name=${c}&view=${v}`);
			const componentData = await response.json();

			componentsData[c][v] = componentData;
		}
	}

	return {
		overview,
		components,
		componentsData
	};
}
