export let apiUrl;

if (import.meta.env.VITE_API_URL) {
  apiUrl = import.meta.env.VITE_API_URL;
} else {
  apiUrl = import.meta.env.DEV ? "http://localhost:3000" : "/api"
}
