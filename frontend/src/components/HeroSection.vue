<script>
export default {
  name: 'HeroSection'
}
</script>


<template>
  <section id="home" class="d-flex align-items-center bg-light-blue py-4 ">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 order-2 order-lg-1 animate-fade-in">
          <span class="badge bg-primary mb-3 px-3 py-2 rounded-pill">Ortho–Neuro Pain Rehabilitation</span>
          <h1 class="display-4 fw-bold mb-4">Dr. Saroj Kumar</h1>
          <h4 class="text-muted mb-4 h5">BPT, MPT, Master Dip. Chiropractic, Radio-BMIT</h4>
          <p class="lead text-secondary mb-5">
            Combining modern radiological understanding with advanced chiropractic techniques for safe, non-surgical pain relief.
          </p>
          <div class="d-flex gap-3 flex-wrap">
            <a href="#contact" class="btn btn-primary btn-lg shadow px-4 py-2 rounded-pill">
              <i class="bi bi-calendar-check me-2"></i> Consult Now
            </a>
            <a href="#services" class="btn btn-outline-primary btn-lg px-4 py-2 rounded-pill">
              View Treatments
            </a>
          </div>
        </div>
        <div class="col-lg-6 order-1 order-lg-2 text-center mb-5 mb-lg-0">
          <div class="position-relative d-inline-block">
            <img src="../asset/img.jpg" 
                 alt="Dr Saroj Kumar" 
                 class="img-fluid rounded-4 shadow-lg border border-5 border-white hero-img">
            
            <div class="card position-absolute bottom-0 start-0 mb-4 ms-n4 border-0 shadow-lg d-none d-md-block" style="width: 200px;">
              <div class="card-body p-3 d-flex align-items-center">
                <div class="bg-success text-white rounded-circle p-2 me-3">
                  <i class="bi bi-shield-check-fill"></i>
                </div>
                <div>
                  <h6 class="mb-0 fw-bold">Verified Expert</h6>
                  <small class="text-muted">Ortho-Neuro</small>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>



<style scoped>
.hero-img {
  object-fit: cover;
  max-height: 600px;
}

</style>