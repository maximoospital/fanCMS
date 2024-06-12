<template>
  <section class="id-contenido">
    <section class="hero">
      <div class="hero-body" style=" padding: 0; margin-bottom: 1.5rem; display:flex; align-items: center;">
        <svg width="647" height="136" viewBox="0 0 647 136" fill="none" xmlns="http://www.w3.org/2000/svg" style="    margin-top: 8px;">
          <path d="M0 38.5H70" stroke="#025373" stroke-width="3"/>
          <text fill="#DFDFDF" xml:space="preserve" style="white-space: pre" font-family="Montserrat" font-size="50" letter-spacing="0em"><tspan x="79" y="48.425">./{{ this.cliente }}</tspan></text>
          <text fill="#F1F1F1" xml:space="preserve" style="white-space: pre" font-family="Montserrat" font-size="55" font-weight="300" letter-spacing="0em"><tspan x="79" y="122.217">{{ this.nombre }}</tspan></text>
        </svg>
        <div class="fila" style="text-align: right;     padding-right: 75px;">
            <b-button @click="updateProduct()" class="button-svg">
              <svg width="178" height="73" viewBox="0 0 178 73" fill="none" xmlns="http://www.w3.org/2000/svg" class="botonsvg2">
                <path d="M0 34C0 16.8792 13.8792 3 31 3H89C106.121 3 120 16.8792 120 34V37C120 54.1208 106.121 68 89 68H31C13.8792 68 0 54.1208 0 37V34Z" fill="#025373" shape-rendering="auto" class="botonsvg2-fondo"/>
                <path d="M28.74 40.12C27.588 40.12 26.684 39.796 26.028 39.148C25.38 38.5 25.056 37.564 25.056 36.34V31.6H26.616V36.28C26.616 37.144 26.8 37.772 27.168 38.164C27.544 38.556 28.072 38.752 28.752 38.752C29.432 38.752 29.956 38.556 30.324 38.164C30.692 37.772 30.876 37.144 30.876 36.28V31.6H32.412V36.34C32.412 37.564 32.084 38.5 31.428 39.148C30.78 39.796 29.884 40.12 28.74 40.12ZM38.5968 40V31.6H42.0528C42.7968 31.6 43.4328 31.72 43.9608 31.96C44.4968 32.2 44.9088 32.544 45.1968 32.992C45.4848 33.44 45.6288 33.972 45.6288 34.588C45.6288 35.204 45.4848 35.736 45.1968 36.184C44.9088 36.632 44.4968 36.976 43.9608 37.216C43.4328 37.456 42.7968 37.576 42.0528 37.576H39.4608L40.1568 36.844V40H38.5968ZM40.1568 37.012L39.4608 36.256H41.9808C42.6688 36.256 43.1848 36.112 43.5287 35.824C43.8808 35.528 44.0568 35.116 44.0568 34.588C44.0568 34.052 43.8808 33.64 43.5287 33.352C43.1848 33.064 42.6688 32.92 41.9808 32.92H39.4608L40.1568 32.152V37.012ZM51.1866 40V31.6H54.8586C55.7706 31.6 56.5706 31.776 57.2586 32.128C57.9466 32.48 58.4826 32.968 58.8666 33.592C59.2506 34.216 59.4426 34.952 59.4426 35.8C59.4426 36.64 59.2506 37.376 58.8666 38.008C58.4826 38.632 57.9466 39.12 57.2586 39.472C56.5706 39.824 55.7706 40 54.8586 40H51.1866ZM52.7466 38.68H54.7866C55.4186 38.68 55.9626 38.56 56.4186 38.32C56.8826 38.08 57.2386 37.744 57.4866 37.312C57.7426 36.88 57.8706 36.376 57.8706 35.8C57.8706 35.216 57.7426 34.712 57.4866 34.288C57.2386 33.856 56.8826 33.52 56.4186 33.28C55.9626 33.04 55.4186 32.92 54.7866 32.92H52.7466V38.68ZM63.7955 40L67.5755 31.6H69.1115L72.9035 40H71.2715L68.0195 32.428H68.6435L65.4035 40H63.7955ZM65.5355 38.056L65.9555 36.832H70.4915L70.9115 38.056H65.5355ZM79.2539 40V32.92H76.4699V31.6H83.5979V32.92H80.8139V40H79.2539ZM90.2086 35.092H94.3846V36.376H90.2086V35.092ZM90.3286 38.692H95.0686V40H88.7686V31.6H94.9006V32.908H90.3286V38.692Z" fill="#F1F1F1" class="botonsvg2-texto"/>
                <g filter="url(#filter0_d_38_588)">
                <circle cx="141.5" cy="35.5" r="31.5" fill="#025373" class="botonsvg2-fondo"/>
                </g>
                <path d="M132.75 26.75H150.25V44.25" stroke="#F1F1F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="botonsvg2-icono"/>
                <path d="M132.75 44.25L150.25 26.75" stroke="#F1F1F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="botonsvg2-icono"/>
              </svg>

            </b-button>
          </div>

      </div>
    </section>
    <form action="" style="width: auto; max-width:89%; margin: auto;">
      <div class="columns">
        <div class="column">
          <h3>Details</h3>
          <div class="rows">
            <div class="row is-full">
              <div class="detalles-filas">
                <div class="detalles-fila">
                  <div class="detalles-columas">
                    <div class="detalles-columa">
                    App
                    </div>
                    <div class="detalles-columa" style="text-align: right; color: #252525;">
                    <b-field>
                        <b-input
                            type="name"
                            v-model="nombre"
                            placeholder="App Name"
                            class="input-detalles"
                            ref="servicio"
                            required
                            >
                        </b-input>
                      </b-field>
                    </div>
                  </div>
                </div>
                <div class="detalles-fila">
                  <div class="detalles-columas">
                    <div class="detalles-columa">
                    Description
                    </div>
                    <div class="detalles-columa" style="text-align: right; color: #252525;     padding-bottom: 5px;">
                    <b-field>
                        <b-input
                            v-model="descripcion"
                            placeholder="Description"
                            class="input-detalles"
                            ref="descripcion"
                            maxlength="120"
                            type="textarea"
                            >
                        </b-input>
                      </b-field>
                    </div>
                  </div>
                </div>
                <div class="detalles-fila">
                  <div class="detalles-columas">
                    <div class="detalles-columa">
                    Client
                    </div>
                    <div class="detalles-columa" style="text-align: right; color: #252525;">
                      <b-field>
                        <b-input
                            type="name"
                            v-model="cliente"
                            placeholder="Client's name"
                            class="input-detalles"
                            ref="nombre"
                            required
                            >
                        </b-input>
                      </b-field>
                    </div>
                  </div>                  
                </div>
                <div class="detalles-fila">
                  <div class="detalles-columas">
                    <div class="detalles-columa">
                    Url
                    </div>
                    <div class="detalles-columa" style="text-align: right; color: #252525;">
                      <b-field>
                        <b-input
                            type="url"
                            v-model="sitio"
                            placeholder="https://client-site.com"
                            class="input-detalles"
                            ref="url"
                            required
                            >
                        </b-input>
                      </b-field>

                    </div>
                  </div>        
                </div>
                <div class="detalles-fila">
                  <div class="detalles-columas">
                    <div class="detalles-columa">
                    Expiration
                    </div>
                    <div class="detalles-columa" style="text-align: right; color: #252525;">
                    <b-field>
                    <b-input
                        type="date"
                        v-model="vencimiento"
                        placeholder="Fecha de Vencimiento"
                        class="input-fecha"
                        ref="fecha"
                        required>
                    </b-input>
                  </b-field>
                    </div>
                  </div>
                </div>
                <div class="detalles-fila">
                  <div class="detalles-columas">
                    <div class="detalles-columa">
                    Admin
                    </div>
                    <div class="detalles-columa" style="text-align: right; color: #252525;">
                    <b-field>
                      <b-input
                        type="email"
                        v-model="administrador"
                        placeholder="Admin"
                        class="input-detalles"
                        ref="email"
                        required>
                    </b-input>
                  </b-field>
                    </div>
                  </div>                  
                </div>
                <div class="detalles-fila">
                  <div class="detalles-columas">
                    <div class="detalles-columa">
                    Plan
                    </div>
                    <div class="detalles-columa" style="text-align: right; color: #252525;">
                      <b-field>
                      <b-select expanded class="input-detalles" v-model="plan" ref="periodo" required>
                        <option hidden>Loading...</option>
                        <option value="mensual">Monthly</option>
                        <option value="anual">Yearly</option>
                      </b-select>
                    </b-field>
                    </div>
                  </div>        
                </div>
                <div class="detalles-fila">
                  <div class="detalles-columas">
                    <div class="detalles-columa" id="campocorto">
                    Auto Renewal
                    </div>
                    <div class="detalles-columa" style="text-align: right; color: #252525;">
                      <b-field>
                        <b-switch v-model="renovacion" ref="renovacion"
                        type="is-danger" style="    margin-bottom: 0px;    margin-right: 0px;">
                        </b-switch>
                      </b-field>
                    </div>
                  </div>        
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="column">
          <h3>Annotations</h3>
          <div class="rows">
            <div class="row is-full">
              <div class="detalles-filas">
                <div class="detalles-fila">
                  <div class="anotaciones-columas">
                    <div class="anotaciones-columa" style="color: #252525;     padding-bottom: 5px;">
                    <b-field>
                        <b-input
                            v-model="anotacion"
                            placeholder="Write your annotation..."
                            class="input-anotacion"
                            ref="anotacion"
                            maxlength="280"
                            type="textarea"
                            >
                        </b-input>
                    </b-field>
                    <b-button @click="comentar()" class="button-svg-2">
                    <svg width="217" height="65" viewBox="0 0 217 65" fill="none" xmlns="http://www.w3.org/2000/svg" class="botonsvg2">
                      <path d="M0 31C0 13.8792 13.8792 0 31 0H186C203.121 0 217 13.8792 217 31V34C217 51.1208 203.121 65 186 65H31C13.8792 65 0 51.1208 0 34V31Z" fill="#025373" shape-rendering="auto" class="botonsvg2-fondo"/>
                      <path d="M23.94 37L27.72 28.6H29.256L33.048 37H31.416L28.164 29.428H28.788L25.548 37H23.94ZM25.68 35.056L26.1 33.832H30.636L31.056 35.056H25.68ZM38.1163 37V28.6H41.7883C42.7003 28.6 43.5003 28.776 44.1883 29.128C44.8763 29.48 45.4123 29.968 45.7963 30.592C46.1803 31.216 46.3723 31.952 46.3723 32.8C46.3723 33.64 46.1803 34.376 45.7963 35.008C45.4123 35.632 44.8763 36.12 44.1883 36.472C43.5003 36.824 42.7003 37 41.7883 37H38.1163ZM39.6763 35.68H41.7163C42.3483 35.68 42.8923 35.56 43.3483 35.32C43.8123 35.08 44.1683 34.744 44.4163 34.312C44.6723 33.88 44.8003 33.376 44.8003 32.8C44.8003 32.216 44.6723 31.712 44.4163 31.288C44.1683 30.856 43.8123 30.52 43.3483 30.28C42.8923 30.04 42.3483 29.92 41.7163 29.92H39.6763V35.68ZM52.0303 37V28.6H55.7023C56.6143 28.6 57.4143 28.776 58.1023 29.128C58.7903 29.48 59.3263 29.968 59.7103 30.592C60.0943 31.216 60.2863 31.952 60.2863 32.8C60.2863 33.64 60.0943 34.376 59.7103 35.008C59.3263 35.632 58.7903 36.12 58.1023 36.472C57.4143 36.824 56.6143 37 55.7023 37H52.0303ZM53.5903 35.68H55.6303C56.2623 35.68 56.8063 35.56 57.2623 35.32C57.7263 35.08 58.0823 34.744 58.3303 34.312C58.5863 33.88 58.7143 33.376 58.7143 32.8C58.7143 32.216 58.5863 31.712 58.3303 31.288C58.0823 30.856 57.7263 30.52 57.2623 30.28C56.8063 30.04 56.2623 29.92 55.6303 29.92H53.5903V35.68ZM72.0728 37L75.8528 28.6H77.3888L81.1808 37H79.5488L76.2968 29.428H76.9208L73.6808 37H72.0728ZM73.8128 35.056L74.2328 33.832H78.7688L79.1888 35.056H73.8128ZM86.2491 37V28.6H87.5331L92.8011 35.068H92.1651V28.6H93.7131V37H92.4291L87.1611 30.532H87.7971V37H86.2491ZM99.9639 37V28.6H101.248L106.516 35.068H105.88V28.6H107.428V37H106.144L100.876 30.532H101.512V37H99.9639ZM117.615 37.12C116.959 37.12 116.355 37.012 115.803 36.796C115.251 36.58 114.771 36.28 114.363 35.896C113.955 35.504 113.639 35.048 113.415 34.528C113.191 34 113.079 33.424 113.079 32.8C113.079 32.176 113.191 31.604 113.415 31.084C113.639 30.556 113.955 30.1 114.363 29.716C114.771 29.324 115.251 29.02 115.803 28.804C116.355 28.588 116.955 28.48 117.603 28.48C118.259 28.48 118.859 28.588 119.403 28.804C119.955 29.02 120.435 29.324 120.843 29.716C121.251 30.1 121.567 30.556 121.791 31.084C122.015 31.604 122.127 32.176 122.127 32.8C122.127 33.424 122.015 34 121.791 34.528C121.567 35.056 121.251 35.512 120.843 35.896C120.435 36.28 119.955 36.58 119.403 36.796C118.859 37.012 118.263 37.12 117.615 37.12ZM117.603 35.752C118.027 35.752 118.419 35.68 118.779 35.536C119.139 35.392 119.451 35.188 119.715 34.924C119.979 34.652 120.183 34.34 120.327 33.988C120.479 33.628 120.555 33.232 120.555 32.8C120.555 32.368 120.479 31.976 120.327 31.624C120.183 31.264 119.979 30.952 119.715 30.688C119.451 30.416 119.139 30.208 118.779 30.064C118.419 29.92 118.027 29.848 117.603 29.848C117.179 29.848 116.787 29.92 116.427 30.064C116.075 30.208 115.763 30.416 115.491 30.688C115.227 30.952 115.019 31.264 114.867 31.624C114.723 31.976 114.651 32.368 114.651 32.8C114.651 33.224 114.723 33.616 114.867 33.976C115.019 34.336 115.227 34.652 115.491 34.924C115.755 35.188 116.067 35.392 116.427 35.536C116.787 35.68 117.179 35.752 117.603 35.752ZM129.367 37V29.92H126.583V28.6H133.711V29.92H130.927V37H129.367ZM137.272 37L141.052 28.6H142.588L146.38 37H144.748L141.496 29.428H142.12L138.88 37H137.272ZM139.012 35.056L139.432 33.832H143.968L144.388 35.056H139.012ZM152.73 37V29.92H149.946V28.6H157.074V29.92H154.29V37H152.73ZM162.245 37V28.6H163.805V37H162.245ZM174.013 37.12C173.357 37.12 172.753 37.012 172.201 36.796C171.649 36.58 171.169 36.28 170.761 35.896C170.353 35.504 170.037 35.048 169.813 34.528C169.589 34 169.477 33.424 169.477 32.8C169.477 32.176 169.589 31.604 169.813 31.084C170.037 30.556 170.353 30.1 170.761 29.716C171.169 29.324 171.649 29.02 172.201 28.804C172.753 28.588 173.353 28.48 174.001 28.48C174.657 28.48 175.257 28.588 175.801 28.804C176.353 29.02 176.833 29.324 177.241 29.716C177.649 30.1 177.965 30.556 178.189 31.084C178.413 31.604 178.525 32.176 178.525 32.8C178.525 33.424 178.413 34 178.189 34.528C177.965 35.056 177.649 35.512 177.241 35.896C176.833 36.28 176.353 36.58 175.801 36.796C175.257 37.012 174.661 37.12 174.013 37.12ZM174.001 35.752C174.425 35.752 174.817 35.68 175.177 35.536C175.537 35.392 175.849 35.188 176.113 34.924C176.377 34.652 176.581 34.34 176.725 33.988C176.877 33.628 176.953 33.232 176.953 32.8C176.953 32.368 176.877 31.976 176.725 31.624C176.581 31.264 176.377 30.952 176.113 30.688C175.849 30.416 175.537 30.208 175.177 30.064C174.817 29.92 174.425 29.848 174.001 29.848C173.577 29.848 173.185 29.92 172.825 30.064C172.473 30.208 172.161 30.416 171.889 30.688C171.625 30.952 171.417 31.264 171.265 31.624C171.121 31.976 171.049 32.368 171.049 32.8C171.049 33.224 171.121 33.616 171.265 33.976C171.417 34.336 171.625 34.652 171.889 34.924C172.153 35.188 172.465 35.392 172.825 35.536C173.185 35.68 173.577 35.752 174.001 35.752ZM184.179 37V28.6H185.463L190.731 35.068H190.095V28.6H191.643V37H190.359L185.091 30.532H185.727V37H184.179Z" fill="#F1F1F1" class="botonsvg2-texto"/>
                    </svg>
                    </b-button>
                    </div>
                  </div>
                </div>
                <div class="detalles-fila">
                  <div class="anotaciones-columas">
                    <div class="anotaciones-columa" style="color: #025373;" id="anotacion">
                      <ul>
                        <li v-for="anotacion in this.anotaciones">
                          <div class="card">
                            <header class="card-header" style="margin-bottom: -45px;">
                              <p class="card-header-title"></p>
                                <b-button @click="eliminarAnotacion(anotacion.commentid)" class="button-svg">
                                    <svg width="20" height="20" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="botonsvg2">
                                      <path d="M2 4H14" stroke="#F1F1F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="botonsvg2-icono"/>
                                      <path d="M12.6667 4V13.3333C12.6667 14 12 14.6667 11.3333 14.6667H4.66667C4 14.6667 3.33333 14 3.33333 13.3333V4" stroke="#F1F1F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="botonsvg2-icono"/>
                                      <path d="M5.33333 4.00001V2.66668C5.33333 2.00001 6 1.33334 6.66667 1.33334H9.33333C10 1.33334 10.6667 2.00001 10.6667 2.66668V4.00001" stroke="#F1F1F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="botonsvg2-icono"/>
                                    </svg>
                                </b-button>
                            </header>
                            <div class="card-content">
                              <div class="content" style="line-height: 1.5rem;padding-right: 2rem;">
                                {{ anotacion.texto }}
                              </div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>                  
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </form>
  </section>
</template>

<script>
  export default {
    layout: 'header',
    data() {
      return {
        nombre: 'Loading...',
        descripcion: 'Loading...',
        plan: null,
        vencimiento: '',
        cliente: 'Loading...',
        sitio: 'Loading...',
        administrador: 'Loading...',
        activo: true,
        renovacion: false,
        id: null,
        anotacion: '',
        anotaciones: []
      }
   },
   head() {
      return {
        title: this.nombre + ' - ' + this.$config.appName
      }
    },
     async mounted () {
      this.str = this.$route.path;
      this.path = this.str.split('/app/')[1];
      console.log(this.path)
      const herramienta = await this.$axios.$get('/herramienta/'+this.path);
      
      const anotaciones = await this.$axios.$get('/comentario/'+this.path);
      this.anotaciones = anotaciones.data;
      console.log(anotaciones.data);
      console.log(herramienta.data);
      this.nombre = herramienta.data.nombre;
      this.descripcion = herramienta.data.descripcion;
      this.plan = herramienta.data.plan;
      this.vencimiento = (new Date(herramienta.data.vencimiento)).toISOString().split('T')[0];
      this.cliente = herramienta.data.cliente;
      this.sitio = herramienta.data.sitio;
      this.administrador = herramienta.data.administrador;
      this.id = this.path;
      if(herramienta.data.activo == 1){
        this.activo = true;
      } else {
        this.activo = false;
      }
      if(herramienta.data.renovacion == 1){
        this.renovacion = true;
      } else {
        this.renovacion = false;
      }
      console.log(this.renovacion);
      console.log(this.activo);
    },
    methods: {
      updateProduct(){
        console.log(this.path);
        console.log("Boton apretado, checkeando");
        this.$refs.nombre.checkHtml5Validity();
        this.$refs.url.checkHtml5Validity();
        this.$refs.email.checkHtml5Validity();
        this.$refs.periodo.checkHtml5Validity();
        this.$refs.servicio.checkHtml5Validity();
        this.$refs.fecha.checkHtml5Validity();
        console.log("Checkeado, avisando al if");
        if (this.$refs.nombre.checkHtml5Validity() && this.$refs.periodo.checkHtml5Validity() && this.$refs.url.checkHtml5Validity() && this.$refs.email.checkHtml5Validity() && this.$refs.servicio.checkHtml5Validity() && this.$refs.fecha.checkHtml5Validity()) {
          console.log("Todo valido, submitteando");
          this.$buefy.toast.open({
              message: 'Actualizando herramienta...',
              type: 'is-success'
          })
          this.submit();
        } else {
          console.log("No va, arreglar. Notificando");
          this.$buefy.toast.open({
              message: 'Herramienta no actualizada, verificar informacion.',
              type: 'is-danger'
          })
        }

      },
     async submit () {
        console.log("Todo valido, enviando");
        const linkup = '/herramienta/' + this.id;
        console.log(linkup);
        const envio = await this.$axios.$put(linkup, {'nombre': this.nombre, 'descripcion': this.descripcion, 'plan': this.plan, 'vencimiento': this.vencimiento, 'cliente': this.cliente, 'sitio': this.sitio, 'administrador': this.administrador, 'activo': this.activo, 'renovacion': this.renovacion }, {crossdomain: true, headers: {"Content-Type": "application/json", "accept": "application/json"}});
        console.log("Enviado, notificando");
        this.$buefy.toast.open({
              message: 'Herramienta actualizada',
              type: 'is-success'
          })
      },
      async comentar () {
        console.log("Enviando comentario");
        const envio_comment = await this.$axios.$post('/comentario/', {'herramienta_id': this.id, 'texto': this.anotacion }, {crossdomain: true, headers: {"Content-Type": "application/json", "accept": "application/json"}});
        const anotacionesupdate = await this.$axios.$get('/comentario/'+this.path);
        this.anotaciones = anotacionesupdate.data;
        console.log(this.anotaciones);
        console.log("Enviado, notificando");
        this.$buefy.toast.open({
              message: 'Annotation made',
              type: 'is-success'
          })
      },      
      async eliminarAnotacion (id) {
        console.log("Eliminando comentario");
        const eliminar_coment = await this.$axios.$delete('/comentario/comment/' + id);      
        const anotacioneseliminadas = this.anotaciones.filter(i => i.commentid !== id);
        this.anotaciones = anotacioneseliminadas;
        this.$buefy.toast.open({
              message: 'Annotation removed',
              type: 'is-success'
          })
      },      

    },
    computed : {
    }
  }

</script>

<style>
  
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600&display=swap');
  
  
  html, body, button, input, optgroup, select, textarea {
    font-family: 'Montserrat', sans-serif !important;
  }
  html {
    background: #1b1b1b !important;
  }

 
</style>
