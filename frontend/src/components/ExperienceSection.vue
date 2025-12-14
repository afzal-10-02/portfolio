<template>
  <section id="experience" class="section-padding bg-light">
    <div class="container">
      <div class="text-center mb-5">
        <h6 class="text-primary fw-bold text-uppercase">Career Timeline</h6>
        <h2 class="fw-bold">Professional Experience</h2>
      </div>
      <div class="row justify-content-center">
        <div class="col-md-8">
          <div class="card mb-4 border-primary border-2 shadow-sm">
            <div class="card-body p-4">
              <div class="d-flex align-items-center flex-column flex-sm-row text-center text-sm-start">
                <div class="bg-primary text-white rounded-circle p-3 mb-3 mb-sm-0 me-sm-4 shadow">
                  <i class="bi bi-hospital fs-3"></i>
                </div>
                <div>
                  <h5 class="card-title fw-bold mb-1">Associated with Back To Nature Spine Clinics</h5>
                  <p class="card-text text-muted mb-1"><i class="bi bi-geo-alt-fill text-danger"></i> Patna, Mumbai, Hyderabad</p>
                  <small class="text-primary bg-light px-2 py-1 rounded">Under guidance of Dr. Rajneesh Kant</small>
                </div>
              </div>
            </div>
          </div>
          <div class="card border-0 shadow-sm">
            <div class="card-header bg-white border-0 pt-4 px-4">
              <h5 class="fw-bold mb-0">Previous Associations</h5>
            </div>
            <div class="card-body p-4">
              <ul class="list-group list-group-flush">
                <li class="list-group-item d-flex justify-content-between align-items-center py-3 border-light">
                  <div><i class="bi bi-building me-2 text-secondary"></i> Apollo Hospital, Bangalore</div>
                  <span class="badge bg-secondary rounded-pill"><i class="bi bi-check"></i></span>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center py-3 border-light">
                  <div><i class="bi bi-building me-2 text-secondary"></i> IGIMS, Patna</div>
                  <span class="badge bg-secondary rounded-pill"><i class="bi bi-check"></i></span>
                </li>
                <li class="list-group-item d-flex justify-content-between align-items-center py-3 border-light">
                  <div><i class="bi bi-building me-2 text-secondary"></i> Mediversal Hospital, Patna</div>
                  <span class="badge bg-secondary rounded-pill"><i class="bi bi-check"></i></span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ExperienceSection'
}

</script>

<style scoped>

#experience{
  max-width: 100%;
}

</style>