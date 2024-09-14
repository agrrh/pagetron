export let isBuildingSnapshot = false;

isBuildingSnapshot = import.meta.env.VITE_BUILD_SNAPSHOT == true;
