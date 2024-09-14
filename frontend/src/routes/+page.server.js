import { apiUrl, getAllData } from '$lib/api.js';
import { isBuildingSnapshot } from '$lib/utils.js';
import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {
	let overview = {};
	let components = [];
	let componentsData = {};

	if (isBuildingSnapshot) {
    return getAllData();
	}

  return { overview, components, componentsData };
}
