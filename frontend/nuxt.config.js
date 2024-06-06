export default {
  /*
  ** Headers of the page
  */
  publicRuntimeConfig: {
    appName: process.env.NUXT_HEAD_TITLE || 'fanCMS',
    axios: {
      baseURL: process.env.NUXT_AXIOS_BASE_URL || 'https://fanapi.maxi.apps-avatar.com'
    }
  },
  head: {
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'ABM en Vue y Nuxt.js para herramientas.' }
    ],
    link: [
        { rel:  'stylesheet prefetch', 
          href: 'https://cdn.jsdelivr.net/npm/@mdi/font@5.8.55/css/materialdesignicons.min.css' }
    ]
  },
  modules: [
    '@nuxtjs/axios',
    '@nuxt/image',
    'nuxt-buefy'
  ],
  axios: {
    proxyHeaders: false,
    credentials: false
  }
}
 