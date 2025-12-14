<template>
  <section id="services" class="section-padding bg-white">
    <div class="container">
      <div class="text-center mb-5">
        <h6 class="text-primary fw-bold text-uppercase">What I Treat</h6>
        <h2 class="fw-bold">Clinical Expertise</h2>
      </div>
      <div class="row g-4">
        <div class="col-md-6 col-lg-4" v-for="(service, index) in services" :key="index">
          <div class="card h-100 border-0 shadow-sm hover-effect bg-light-blue">
            <div class="card-body text-center p-4">
              <div class="bg-white rounded-circle d-inline-flex p-3 mb-3 text-primary shadow-sm icon-wrapper">
                <i :class="service.icon" style="font-size: 2rem;"></i>
              </div>
              <h5 class="card-title fw-bold mb-3">{{ service.title }}</h5>
              <p class="card-text text-secondary small">{{ service.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ServicesSection',
  data() {
    return {
      services: [
        { title: 'Back & Neck Pain', desc: 'Specialized chiropractic adjustments for chronic pain relief.', icon: 'bi bi-person-standing' },
        { title: 'Slip Disc / Sciatica', desc: 'Non-surgical management of disc bulges and nerve pain.', icon: 'bi bi-activity' },
        { title: 'Paralysis Rehab', desc: 'Evidence-based rehabilitation for neurological recovery.', icon: 'bi bi-bandaid' },
        { title: 'Joint Pain', desc: 'Treatment for stiffness, arthritis, and mobility issues.', icon: 'bi bi-diagram-3' },
        { title: 'Sports Injuries', desc: 'Rapid recovery protocols for athletic injuries.', icon: 'bi bi-bicycle' },
        { title: 'Migraine & Headache', desc: 'Addressing cervical causes of chronic headaches.', icon: 'bi bi-emoji-dizzy' },
      ]
    }
  }
}
</script>

<style scoped>
.hover-effect {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.hover-effect:hover {
  transform: translateY(-5px);
  box-shadow: 0 .5rem 1rem rgba(0,0,0,.15)!important;
}
.icon-wrapper {
  width: 80px; 
  height: 80px; 
  align-items: center; 
  justify-content: center;
}
#services{
  max-width: 100%;
}
</style>