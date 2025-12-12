<template>
  <section id="contact" class="section-padding bg-light-blue">
    <div class="container">
      <div class="row g-5">
        <div class="col-lg-7">
          <div class="card border-0 shadow rounded-4 overflow-hidden h-100">
            <div class="card-body p-5">
              <h3 class="fw-bold mb-2 text-primary">Book an Appointment</h3>
              <p class="text-muted mb-4">Fill out the form below and we will get back to you shortly.</p>
              
              <form @submit.prevent="submitForm">
                <div class="row g-3">
                  <div class="col-md-6">
                    <label class="form-label small text-uppercase fw-bold text-secondary">Your Name</label>
                    <input type="text" class="form-control form-control-lg bg-light border-0" v-model="form.name" placeholder="John Doe" required>
                  </div>
                  <div class="col-md-6">
                    <label class="form-label small text-uppercase fw-bold text-secondary">Phone Number</label>
                    <input type="tel" class="form-control form-control-lg bg-light border-0" v-model="form.phone" placeholder="+91 98765..." required>
                  </div>
                  <div class="col-12">
                    <label class="form-label small text-uppercase fw-bold text-secondary">Email Address</label>
                    <input type="email" class="form-control form-control-lg bg-light border-0" v-model="form.email" placeholder="name@example.com" required>
                  </div>
                  <div class="col-12">
                    <label class="form-label small text-uppercase fw-bold text-secondary">Your Message</label>
                    <textarea class="form-control form-control-lg bg-light border-0" v-model="form.message" rows="4" placeholder="Tell us about your pain or preferred appointment time..." required></textarea>
                  </div>
                  <div class="col-12 mt-4">
                    <button type="submit" class="btn btn-primary btn-lg w-100 rounded-pill fw-bold">
                      <i class="bi bi-send-fill me-2"></i> Send Request
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>

        <div class="col-lg-5">
          <div class="h-100 d-flex flex-column justify-content-center">
            <h2 class="fw-bold mb-4">Get in Touch</h2>
            <p class="text-secondary lead mb-5">
              Visit one of our clinics or contact us directly for immediate assistance with acute or chronic pain.
            </p>
            <div class="d-flex mb-4">
              <div class="bg-primary bg-opacity-10 text-primary rounded-circle p-3 me-3 icon-circle">
                <i class="bi bi-geo-alt-fill fs-4"></i>
              </div>
              <div>
                <h5 class="fw-bold mb-1">Clinic Locations</h5>
                <p class="text-muted mb-0">Back To Nature Spine Clinics<br>Patna, Mumbai, Hyderabad</p>
              </div>
            </div>
            <div class="d-flex mb-4">
              <div class="bg-primary bg-opacity-10 text-primary rounded-circle p-3 me-3 icon-circle">
                <i class="bi bi-envelope-fill fs-4"></i>
              </div>
              <div>
                <h5 class="fw-bold mb-1">Email Us</h5>
                <p class="text-muted mb-0">appointment@drsarojkumar.com</p>
              </div>
            </div>
            <div class="d-flex mb-4">
              <div class="bg-primary bg-opacity-10 text-primary rounded-circle p-3 me-3 icon-circle">
                <i class="bi bi-telephone-fill fs-4"></i>
              </div>
              <div>
                <h5 class="fw-bold mb-1">Call Us</h5>
                <p class="text-muted mb-0">+91 98765 43210</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ContactSection',
  data() {
    return {
      form: {
        name: '',
        phone: '',
        email: '',
        message: ''
      }
    }
  },
  methods: {
    submitForm() {
      // Logic to handle form submission
      alert(`Thank you ${this.form.name}! Your request has been received. We will contact you at ${this.form.phone} shortly.`);
      // Reset form
      this.form = { name: '', phone: '', email: '', message: '' };
    }
  }
}
</script>

<style scoped>
.form-control:focus {
  border-color: #0d6efd;
  box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.15);
}
.icon-circle {
  width: 60px; 
  height: 60px; 
  display: flex; 
  align-items: center; 
  justify-content: center;
}
</style>