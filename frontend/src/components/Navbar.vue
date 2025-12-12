<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top shadow-sm">
    <div class="container">
      <a class="navbar-brand fw-bold d-flex align-items-center" href="#home">
        <i class="bi bi-activity me-1"></i> Dr. Saroj Kumar
      </a>
      
      <button 
        class="navbar-toggler" 
        type="button" 
        data-bs-toggle="collapse" 
        data-bs-target="#navbarNav"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav align-items-center">
          <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
          <li class="nav-item"><a class="nav-link" href="#experience">Experience</a></li>
          <li class="nav-item"><a class="nav-link" href="#services">Expertise</a></li>
          <li class="nav-item">
            <a class="nav-link btn ms-lg-3 px-4 rounded-pill fw-bold custom-book-btn" href="#contact">
              Book Appointment
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
.btn {
    color: black;
}

.navbar-brand {
  letter-spacing: 0.5px;
}
.nav-link {
  cursor: pointer;
  font-weight: 500;
}
.custom-book-btn {
  color: black !important;
}
</style>