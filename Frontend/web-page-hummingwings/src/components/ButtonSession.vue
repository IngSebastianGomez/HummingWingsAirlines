<template>
    <div class="row align-items-start" style="padding-right: 1rem;">
        <button type="button"
                class="btn btn-primary"
                style="background-color: #182a3f; border: 0px;"
                @click="navigateToLogin">Iniciar Sesión</button>
    </div>
</template>

<script>
export default {
    methods: {
        navigateToLogin() {
            this.$router.push('/LoginUser');
        }
    }
}
</script>

  