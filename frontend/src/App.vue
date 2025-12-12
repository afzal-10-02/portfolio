<template>
  <div id="app">
    <Navbar />
    <HeroSection />
    <AboutSection />
    <ExperienceSection />
    <ServicesSection />
    <ContactSection />
    <Footer />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import HeroSection from './components/HeroSection.vue'
import AboutSection from './components/AboutSection.vue'
import ExperienceSection from './components/ExperienceSection.vue'
import ServicesSection from './components/ServicesSection.vue'
import ContactSection from './components/ContactSection.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    HeroSection,
    AboutSection,
    ExperienceSection,
    ServicesSection,
    ContactSection,
    Footer
  }
}
</script>

<style>
/* Global Styles */
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
  overflow-x: hidden;
}

.section-padding {
  padding: 80px 0;
}

.bg-light-blue {
  background-color: #f0f8ff;
}

/* Scroll Behavior for smooth anchor jumping */
html {
  scroll-behavior: smooth;
  scroll-padding-top: 70px; /* Offsets the fixed navbar */
}
</style>