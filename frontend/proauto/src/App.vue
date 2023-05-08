<template>

  <main>
    <!-- <ServicesPage />
    <ImagesPage /> -->
    <ServicesPage />
  </main>
  
</template>


<script>
import ServicesPage from './components/ServicesPage.vue'
import ImagesPage from './components/ImagesPage.vue'
export default {
  name: "App",
  components: {
    ServicesPage, ImagesPage
  },
};
</script>
  