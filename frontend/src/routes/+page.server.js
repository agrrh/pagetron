import { apiUrl, getAllData } from '$lib/api.js';
import { toImportData } from '$lib/utils.js';
import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {
	let overview = {};
	let components = [];
	let componentsData = {};

	if (toImportData) {
    return getAllData();
	}

  return { overview, components, componentsData };
}
