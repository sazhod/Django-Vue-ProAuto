/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,jsx}",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
    colors: {
      'main': '#fde047',
      'bg': '#1e293b',
      'hovered-bg': '#64748b',
      'menu-bg': '#0f172a',
      'menu-border': '#334155',
      'text': '#f1f5f9',
      'dark-text': '#0f172a',
      '2gis': '#84cc16',
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],

}

