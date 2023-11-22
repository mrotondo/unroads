import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
  base: '/unroads/',
  server: {
    hmr:
      process.env.CODESANDBOX_SSE || process.env.GITPOD_WORKSPACE_ID
        ? 443
        : undefined,
  },
});
