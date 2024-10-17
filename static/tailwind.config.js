/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
      '../main/templates/**/*.html',
      '../main/templates/template_parts/**/*.html',
      './node_modules/flowbite/**/*.js',
      '../static/scripts/**/*.js',
      './node_modules/preline/dist/*.js'

  ],
  theme: {
    extend: {},
    colors:{
      'main': {
        DEFAULT: '#1B2741',
        light: '#5F687A',
        dark: '#075985',
    }}
  },
  plugins: [
    require('flowbite/plugin'),
    require('preline/plugin'),
    require('@tailwindcss/aspect-ratio'),
        require('tailwindcss/plugin')(function({ addVariant }) {
      addVariant('children', '&>*');
      addVariant('h2', '&>h2');
      addVariant('h3', '&>h3');
      addVariant('h4', '&>h4');
      addVariant('p', '&>p');
    })
  ],
}