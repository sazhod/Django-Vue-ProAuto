/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,jsx}",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
    // colors: {
    //   'main': '#fde047',
    //   'bg': '#1e293b',
    //   'hovered-bg': '#64748b',
    //   'menu-bg': '#0f172a',
    //   'menu-border': '#334155',
    //   'text': '#f1f5f9',
    //   'dark-text': '#0f172a',
    //   '2gis': '#84cc16',
    // },
    colors: {
      'main': '#fde047',
      'bg': '#181818',
      'hovered-bg': '#64748b',
      'menu-bg': '#141414',
      'menu-border': '#334155',
      'card-bg': '#222222',
      'card-border': '#334155',
      'text': '#f1f5f9',
      'text-gray': '#bdbdbd',
      'dark-text': '#0f172a',
      '2gis': '#84cc16',
    },
    blur: {
      xs: '1px',
    },
    fontSize: {
      'mobile-head': '20px',
      'mobile-body': '10px',

      'mobile-card-head': '15px',
      'mobile-card-body': '12px',

      'desktop-head': '40px',
      'desktop-body': '16px',

      'desktop-card-head': '25px',
      'desktop-card-body': '15px',
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],

}

