<template>
  <nav id="nav" class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top shadow-sm">
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
          <li class="nav-item"><a class="nav-link" @click="closeMenu" href="#home">Home</a></li>
          <li class="nav-item"><a class="nav-link" @click="closeMenu" href="#about">About</a></li>
          <li class="nav-item"><a class="nav-link" @click="closeMenu" href="#experience">Experience</a></li>
          <li class="nav-item"><a class="nav-link" @click="closeMenu" href="#services">Expertise</a></li>
          <li class="nav-item">
            <a class="nav-link btn ms-lg-3 px-4 rounded-pill fw-bold custom-book-btn contact" @click="closeMenu" href="#contact">
              Book Appointment
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <div ref="gapRef" class="gap">

  </div>
</template>

<script >
export default {
  name: 'Navbar',
  mounted() {
    // Calculate height when component loads
    this.adjustGapHeight();
    // Recalculate if user resizes window (e.g. rotates phone)
    window.addEventListener('resize', this.adjustGapHeight);
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.adjustGapHeight);
  },
  methods: {
    adjustGapHeight() {
      const navbar = this.$refs.navbarRef;
      const gapDiv = this.$refs.gapRef;

      if (navbar && gapDiv) {
        // 1. Get exact height of the navbar
        const navHeight = navbar.offsetHeight;
        // 2. Push the content down by that amount
        gapDiv.style.height = `${navHeight}px`;
      }
    },

    closeMenu() {
      // Get the navbar collapse element
      const navCollapse = document.getElementById('navbarNav');
      
      // Check if the menu is open (has the 'show' class)
      if (navCollapse && navCollapse.classList.contains('show')) {
        // Use the global Bootstrap object to toggle it closed
        // We use window.bootstrap because you are loading it via CDN in index.html
        const bsCollapse = new window.bootstrap.Collapse(navCollapse, {
          toggle: false
        });
        bsCollapse.hide();
      }
    }
}}

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
  color: white;
  border: 2px solid transparent;
  border-radius: 25px;
}

.nav-link:hover{
  border: 2px solid white;
  border-radius: 25px;
}

.nav-link{
  padding: 5px;
  margin: 0;
}

.custom-book-btn {
  color: black !important;
}

.contact{
  background-color: White;
}
.gap {
  height: 60px; 
  display: block;
}

</style>