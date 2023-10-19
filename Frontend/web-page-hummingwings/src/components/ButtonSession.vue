<template>
        <div class="btn-group">
            <button type="button" class="btn btn-primary" @click="navigateToLogin">Iniciar Sesión</button>
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

  