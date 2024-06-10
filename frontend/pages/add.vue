<template>
    <section class="contenido">
      <section class="hero">
        <div class="hero-body" style=" padding: 0; margin-bottom: 1.5rem;">
          <svg width="948" height="110" viewBox="0 0 948 110" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M0 69.5H70" stroke="#025373" stroke-width="3"/>
          <text fill="#f1f1f1" xml:space="preserve" style="white-space: pre" font-family="Montserrat" font-size="55" font-weight="bold" letter-spacing="0em"><tspan x="79" y="85.2175">Add App</tspan></text>
          </svg>
        </div>
      </section>
      <section action="" style="width: auto; max-width:89%; margin: auto;">
        <form action="">
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
                            placeholder="App name"
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
                    Client
                    </div>
                    <div class="detalles-columa" style="text-align: right; color: #252525;">
                      <b-field>
                        <b-input
                            type="name"
                            v-model="cliente"
                            placeholder="Client name"
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
                    Description (opcional)
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

              </div>
            </div>
          </div>
        </div>
        <div class="column">
          <h3>Subscription</h3>
          <div class="rows">
            <div class="detalles-fila">
                  <div class="detalles-columas">
                    <div class="detalles-columa">
                    Subscription Date
                    </div>
                    <div class="detalles-columa" style="text-align: right; color: #252525;">
                    <b-field>
                    <b-input
                        type="date"
                        v-model="vencimiento"
                        placeholder="Subscription Date"
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
                        placeholder="Admin's email"
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
                      <b-select expanded class="input-detalles" placeholder="Select a plan" v-model="plan" ref="periodo" required>
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
                    Ren. Automatica
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
    </form>
          <div class="fila" style="text-align: right; padding-top: 4em;">
            <!-- <b-button @click="$router.push('/')" class="button-svg"> -->
            <a href="/" class="button button-svg">
              <svg width="120" height="65" viewBox="0 0 120 65" fill="none" xmlns="http://www.w3.org/2000/svg" class="botonsvg">
                <path d="M0 31C0 13.8792 13.8792 0 31 0H89C106.121 0 120 13.8792 120 31V34C120 51.1208 106.121 65 89 65H31C13.8792 65 0 51.1208 0 34V31Z" fill="#025373" class="botonsvg-fondo"/>
                <path d="M29.016 37.12C28.376 37.12 27.78 37.016 27.228 36.808C26.684 36.592 26.208 36.292 25.8 35.908C25.4 35.516 25.088 35.056 24.864 34.528C24.64 34 24.528 33.424 24.528 32.8C24.528 32.176 24.64 31.6 24.864 31.072C25.088 30.544 25.404 30.088 25.812 29.704C26.22 29.312 26.696 29.012 27.24 28.804C27.784 28.588 28.38 28.48 29.028 28.48C29.716 28.48 30.344 28.6 30.912 28.84C31.48 29.072 31.96 29.42 32.352 29.884L31.344 30.832C31.04 30.504 30.7 30.26 30.324 30.1C29.948 29.932 29.54 29.848 29.1 29.848C28.66 29.848 28.256 29.92 27.888 30.064C27.528 30.208 27.212 30.412 26.94 30.676C26.676 30.94 26.468 31.252 26.316 31.612C26.172 31.972 26.1 32.368 26.1 32.8C26.1 33.232 26.172 33.628 26.316 33.988C26.468 34.348 26.676 34.66 26.94 34.924C27.212 35.188 27.528 35.392 27.888 35.536C28.256 35.68 28.66 35.752 29.1 35.752C29.54 35.752 29.948 35.672 30.324 35.512C30.7 35.344 31.04 35.092 31.344 34.756L32.352 35.716C31.96 36.172 31.48 36.52 30.912 36.76C30.344 37 29.712 37.12 29.016 37.12ZM36.483 37L40.263 28.6H41.799L45.591 37H43.959L40.707 29.428H41.331L38.091 37H36.483ZM38.223 35.056L38.643 33.832H43.179L43.599 35.056H38.223ZM50.6593 37V28.6H51.9433L57.2113 35.068H56.5753V28.6H58.1233V37H56.8393L51.5713 30.532H52.2073V37H50.6593ZM68.2621 37.12C67.6221 37.12 67.0261 37.016 66.4741 36.808C65.9301 36.592 65.4541 36.292 65.0461 35.908C64.6461 35.516 64.3341 35.056 64.1101 34.528C63.8861 34 63.7741 33.424 63.7741 32.8C63.7741 32.176 63.8861 31.6 64.1101 31.072C64.3341 30.544 64.6501 30.088 65.0581 29.704C65.4661 29.312 65.9421 29.012 66.4861 28.804C67.0301 28.588 67.6261 28.48 68.2741 28.48C68.9621 28.48 69.5901 28.6 70.1581 28.84C70.7261 29.072 71.2061 29.42 71.5981 29.884L70.5901 30.832C70.2861 30.504 69.9461 30.26 69.5701 30.1C69.1941 29.932 68.7861 29.848 68.3461 29.848C67.9061 29.848 67.5021 29.92 67.1341 30.064C66.7741 30.208 66.4581 30.412 66.1861 30.676C65.9221 30.94 65.7141 31.252 65.5621 31.612C65.4181 31.972 65.3461 32.368 65.3461 32.8C65.3461 33.232 65.4181 33.628 65.5621 33.988C65.7141 34.348 65.9221 34.66 66.1861 34.924C66.4581 35.188 66.7741 35.392 67.1341 35.536C67.5021 35.68 67.9061 35.752 68.3461 35.752C68.7861 35.752 69.1941 35.672 69.5701 35.512C69.9461 35.344 70.2861 35.092 70.5901 34.756L71.5981 35.716C71.2061 36.172 70.7261 36.52 70.1581 36.76C69.5901 37 68.9581 37.12 68.2621 37.12ZM78.5328 32.092H82.7088V33.376H78.5328V32.092ZM78.6528 35.692H83.3928V37H77.0928V28.6H83.2248V29.908H78.6528V35.692ZM89.1319 37V28.6H90.6919V35.68H95.0839V37H89.1319Z" fill="#F1F1F1" class="botonsvg-texto"/>
              </svg>
            </a>
            <!-- </b-button> -->
            <b-button @click="createProduct()" class="button-svg">
              <svg width="189" height="73" viewBox="0 0 189 73" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-top: 0.5em;" class="botonsvg2">
                <path d="M0 34C0 16.8792 13.8792 3 31 3H100C117.121 3 131 16.8792 131 34V37C131 54.1208 117.121 68 100 68H31C13.8792 68 0 54.1208 0 37V34Z" fill="#025373" shape-rendering="auto" class="botonsvg2-fondo"/>
                <path d="M23.94 40L27.72 31.6H29.256L33.048 40H31.416L28.164 32.428H28.788L25.548 40H23.94ZM25.68 38.056L26.1 36.832H30.636L31.056 38.056H25.68ZM38.1163 40V31.6H41.7883C42.7003 31.6 43.5003 31.776 44.1883 32.128C44.8763 32.48 45.4123 32.968 45.7963 33.592C46.1803 34.216 46.3723 34.952 46.3723 35.8C46.3723 36.64 46.1803 37.376 45.7963 38.008C45.4123 38.632 44.8763 39.12 44.1883 39.472C43.5003 39.824 42.7003 40 41.7883 40H38.1163ZM39.6763 38.68H41.7163C42.3483 38.68 42.8923 38.56 43.3483 38.32C43.8123 38.08 44.1683 37.744 44.4163 37.312C44.6723 36.88 44.8003 36.376 44.8003 35.8C44.8003 35.216 44.6723 34.712 44.4163 34.288C44.1683 33.856 43.8123 33.52 43.3483 33.28C42.8923 33.04 42.3483 32.92 41.7163 32.92H39.6763V38.68ZM52.0303 40V31.6H55.7023C56.6143 31.6 57.4143 31.776 58.1023 32.128C58.7903 32.48 59.3263 32.968 59.7103 33.592C60.0943 34.216 60.2863 34.952 60.2863 35.8C60.2863 36.64 60.0943 37.376 59.7103 38.008C59.3263 38.632 58.7903 39.12 58.1023 39.472C57.4143 39.824 56.6143 40 55.7023 40H52.0303ZM53.5903 38.68H55.6303C56.2623 38.68 56.8063 38.56 57.2623 38.32C57.7263 38.08 58.0823 37.744 58.3303 37.312C58.5863 36.88 58.7143 36.376 58.7143 35.8C58.7143 35.216 58.5863 34.712 58.3303 34.288C58.0823 33.856 57.7263 33.52 57.2623 33.28C56.8063 33.04 56.2623 32.92 55.6303 32.92H53.5903V38.68ZM72.0728 40L75.8528 31.6H77.3888L81.1808 40H79.5488L76.2968 32.428H76.9208L73.6808 40H72.0728ZM73.8128 38.056L74.2328 36.832H78.7688L79.1888 38.056H73.8128ZM86.2491 40V31.6H89.7051C90.4491 31.6 91.0851 31.72 91.6131 31.96C92.1491 32.2 92.5611 32.544 92.8491 32.992C93.1371 33.44 93.2811 33.972 93.2811 34.588C93.2811 35.204 93.1371 35.736 92.8491 36.184C92.5611 36.632 92.1491 36.976 91.6131 37.216C91.0851 37.456 90.4491 37.576 89.7051 37.576H87.1131L87.8091 36.844V40H86.2491ZM87.8091 37.012L87.1131 36.256H89.6331C90.3211 36.256 90.8371 36.112 91.1811 35.824C91.5331 35.528 91.7091 35.116 91.7091 34.588C91.7091 34.052 91.5331 33.64 91.1811 33.352C90.8371 33.064 90.3211 32.92 89.6331 32.92H87.1131L87.8091 32.152V37.012ZM98.8389 40V31.6H102.295C103.039 31.6 103.675 31.72 104.203 31.96C104.739 32.2 105.151 32.544 105.439 32.992C105.727 33.44 105.871 33.972 105.871 34.588C105.871 35.204 105.727 35.736 105.439 36.184C105.151 36.632 104.739 36.976 104.203 37.216C103.675 37.456 103.039 37.576 102.295 37.576H99.7029L100.399 36.844V40H98.8389ZM100.399 37.012L99.7029 36.256H102.223C102.911 36.256 103.427 36.112 103.771 35.824C104.123 35.528 104.299 35.116 104.299 34.588C104.299 34.052 104.123 33.64 103.771 33.352C103.427 33.064 102.911 32.92 102.223 32.92H99.7029L100.399 32.152V37.012Z" fill="#F1F1F1" class="botonsvg2-texto"/>
                <g filter="url(#filter0_d_39_588)">
                <circle cx="152.5" cy="35.5" r="31.5" fill="#025373" class="botonsvg2-fondo"/>
                </g>
                <path d="M143.75 26.75H161.25V44.25" stroke="#F1F1F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="botonsvg2-icono"/>
                <path d="M143.75 44.25L161.25 26.75" stroke="#F1F1F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="botonsvg2-icono"/>
              </svg>
            </b-button>
          </div>
      </section>
              <b-modal v-model="isCardModalActive" :width="750" :can-cancel="false" scroll="clip">
            <div class="card" style="background-color: #252525; border-radius: 1.25rem;">
                <div class="card-content">
                    <div class="media">
                        <div class="media-content">
                            <p style="font-size: 2.5rem; font-family: 'Montserrat'; font-weight: 600; color:#A4A4A4;">App added!</p>
                        </div>
                    </div>
                    <div class="content">
                      <div class="card" style="border-radius: 1.25rem; box-shadow: none; -webkit-box-shadow: none; color: #A4A4A4; border: 1.5px solid;">
                        <div class="card-content">
                          <div class="content">
                            <div class="columns">
                              <div class="column is-11 column2"><h3 style="font-weight: 400; color: #A4A4A4; font-size: 1.5rem;">{{ this.cliente }} - {{ this.nombre }}</h3></div>
                              <div class="column column2" style="max-width: 100%; text-align: right;">
                                <b-button @click="redirect()" class="button-svg" style="height: fit-content;">
                                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                                  <g clip-path="url(#clip0_25_10)">
                                  <path d="M11.3333 2.00001C11.5031 1.79936 11.7131 1.63605 11.95 1.52046C12.1869 1.40488 12.4454 1.33956 12.7091 1.32868C12.9728 1.3178 13.2359 1.36159 13.4816 1.45727C13.7273 1.55294 13.9503 1.69839 14.1362 1.88435C14.3222 2.07032 14.4671 2.29272 14.5617 2.53737C14.6563 2.78202 14.6986 3.04356 14.6857 3.30533C14.6729 3.56709 14.6053 3.82333 14.4873 4.05772C14.3692 4.29211 14.2033 4.4995 14 4.66667L5.00001 13.6667L1.33334 14.6667L2.33334 11L11.3333 2.00001Z" stroke="#F1F1F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                  <path d="M10 3.33334L12.6667 6.00001" stroke="#F1F1F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                  </g>
                                  <defs>
                                  <clipPath id="clip0_25_10">
                                  <rect width="16" height="16" fill="white"/>
                                  </clipPath>
                                  </defs>
                                </svg>
                                </b-button>
                              </div>
                            </div>
                            <div class="columns">
                              <div class="column is-6 column2">
                                <p style="font-size: 1rem; font-weight: 400; color: #A4A4A4;">Admin</p>
                                </div>
                              <div class="column column2">
                                <p style="font-size: 1rem; font-weight: 400; text-align: right;">{{ this.administrador }}</p>
                              </div>
                            </div>                            
                            <div class="columns">
                              <div class="column is-6 column2">
                                <p style="font-size: 1rem; font-weight: 400; color: #A4A4A4;">Renovation date</p>
                                </div>
                              <div class="column column2">
                                <p style="font-size: 1rem; font-weight: 400; text-align: right;">{{ this.fechafinal }}</p>
                              </div>
                            </div>                            
                            <div class="columns">
                              <div class="column is-6 column2">
                                <p style="font-size: 1rem; font-weight: 400; color: #A4A4A4;">Auto Renewal</p>
                                </div>
                              <div class="column column2">
                                <p style="font-size: 1rem; font-weight: 400; text-align: right;" v-if="this.renovacion">Yes</p>
                                <p style="font-size: 1rem; font-weight: 400; text-align: right;" v-if="!this.renovacion">No</p>
                              </div>
                            </div>                            
                            
                            <div class="columns">
                              <div class="column is-6 column2">
                                <p style="font-size: 1rem; font-weight: 400; color: #A4A4A4;">URL</p>
                                </div>
                              <div class="column column2">
                                <a :href="this.sitio"><p style="font-size: 1rem; font-weight: 400; text-align: right;">{{ this.sitio }}</p></a>
                              </div>
                            </div>                            
                          </div>
                        </div>
                      </div>
                      <br>
                      <div style="text-align: center;">
                        <a href="/" class="button button-svg" style="padding-bottom: 1%;">
                          <svg width="94" height="65" viewBox="0 0 94 65" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M0 31C0 13.8792 13.8792 0 31 0H63C80.1208 0 94 13.8792 94 31V34C94 51.1208 80.1208 65 63 65H31C13.8792 65 0 51.1208 0 34V31Z" fill="#025373"/>
                            <path d="M23.94 37L27.72 28.6H29.256L33.048 37H31.416L28.164 29.428H28.788L25.548 37H23.94ZM25.68 35.056L26.1 33.832H30.636L31.056 35.056H25.68ZM38.1163 37V28.6H41.5723C42.3163 28.6 42.9523 28.72 43.4803 28.96C44.0163 29.2 44.4283 29.544 44.7163 29.992C45.0043 30.44 45.1483 30.972 45.1483 31.588C45.1483 32.204 45.0043 32.736 44.7163 33.184C44.4283 33.632 44.0163 33.976 43.4803 34.216C42.9523 34.456 42.3163 34.576 41.5723 34.576H38.9803L39.6763 33.844V37H38.1163ZM39.6763 34.012L38.9803 33.256H41.5003C42.1883 33.256 42.7043 33.112 43.0483 32.824C43.4003 32.528 43.5763 32.116 43.5763 31.588C43.5763 31.052 43.4003 30.64 43.0483 30.352C42.7043 30.064 42.1883 29.92 41.5003 29.92H38.9803L39.6763 29.152V34.012ZM50.7061 37V28.6H54.1621C54.9061 28.6 55.5421 28.72 56.0701 28.96C56.6061 29.2 57.0181 29.544 57.3061 29.992C57.5941 30.44 57.7381 30.972 57.7381 31.588C57.7381 32.204 57.5941 32.736 57.3061 33.184C57.0181 33.632 56.6061 33.976 56.0701 34.216C55.5421 34.456 54.9061 34.576 54.1621 34.576H51.5701L52.2661 33.844V37H50.7061ZM52.2661 34.012L51.5701 33.256H54.0901C54.7781 33.256 55.2941 33.112 55.6381 32.824C55.9901 32.528 56.1661 32.116 56.1661 31.588C56.1661 31.052 55.9901 30.64 55.6381 30.352C55.2941 30.064 54.7781 29.92 54.0901 29.92H51.5701L52.2661 29.152V34.012ZM66.0172 37.12C65.3612 37.12 64.7332 37.028 64.1332 36.844C63.5332 36.652 63.0572 36.408 62.7052 36.112L63.2452 34.9C63.5812 35.164 63.9972 35.384 64.4932 35.56C64.9892 35.736 65.4972 35.824 66.0172 35.824C66.4572 35.824 66.8132 35.776 67.0852 35.68C67.3572 35.584 67.5572 35.456 67.6852 35.296C67.8132 35.128 67.8772 34.94 67.8772 34.732C67.8772 34.476 67.7852 34.272 67.6012 34.12C67.4172 33.96 67.1772 33.836 66.8812 33.748C66.5932 33.652 66.2692 33.564 65.9092 33.484C65.5572 33.404 65.2012 33.312 64.8412 33.208C64.4892 33.096 64.1652 32.956 63.8692 32.788C63.5812 32.612 63.3452 32.38 63.1612 32.092C62.9772 31.804 62.8852 31.436 62.8852 30.988C62.8852 30.532 63.0052 30.116 63.2452 29.74C63.4932 29.356 63.8652 29.052 64.3612 28.828C64.8652 28.596 65.5012 28.48 66.2692 28.48C66.7732 28.48 67.2732 28.544 67.7692 28.672C68.2652 28.8 68.6972 28.984 69.0652 29.224L68.5732 30.436C68.1972 30.212 67.8092 30.048 67.4092 29.944C67.0092 29.832 66.6252 29.776 66.2572 29.776C65.8252 29.776 65.4732 29.828 65.2012 29.932C64.9372 30.036 64.7412 30.172 64.6132 30.34C64.4932 30.508 64.4332 30.7 64.4332 30.916C64.4332 31.172 64.5212 31.38 64.6972 31.54C64.8812 31.692 65.1172 31.812 65.4052 31.9C65.7012 31.988 66.0292 32.076 66.3892 32.164C66.7492 32.244 67.1052 32.336 67.4572 32.44C67.8172 32.544 68.1412 32.68 68.4292 32.848C68.7252 33.016 68.9612 33.244 69.1372 33.532C69.3212 33.82 69.4132 34.184 69.4132 34.624C69.4132 35.072 69.2892 35.488 69.0412 35.872C68.8012 36.248 68.4292 36.552 67.9252 36.784C67.4212 37.008 66.7852 37.12 66.0172 37.12Z" fill="#F1F1F1"/>
                          </svg>
                        </a>
                        <!-- <b-button @click="cancelProduct()" class="button-svg">
                          <svg width="234" height="64" viewBox="0 0 234 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="0.5" y="0.5" width="233" height="63" rx="30.5" fill="white"/>
                            <rect x="0.5" y="0.5" width="233" height="63" rx="30.5" stroke="#025373"/>
                            <path d="M27.612 36.5L23.94 28.1H25.632L28.908 35.696H27.936L31.248 28.1H32.808L29.148 36.5H27.612ZM41.5484 36.62C40.8924 36.62 40.2884 36.512 39.7364 36.296C39.1844 36.08 38.7044 35.78 38.2964 35.396C37.8884 35.004 37.5724 34.548 37.3484 34.028C37.1244 33.5 37.0124 32.924 37.0124 32.3C37.0124 31.676 37.1244 31.104 37.3484 30.584C37.5724 30.056 37.8884 29.6 38.2964 29.216C38.7044 28.824 39.1844 28.52 39.7364 28.304C40.2884 28.088 40.8884 27.98 41.5364 27.98C42.1924 27.98 42.7924 28.088 43.3364 28.304C43.8884 28.52 44.3684 28.824 44.7764 29.216C45.1844 29.6 45.5004 30.056 45.7244 30.584C45.9484 31.104 46.0604 31.676 46.0604 32.3C46.0604 32.924 45.9484 33.5 45.7244 34.028C45.5004 34.556 45.1844 35.012 44.7764 35.396C44.3684 35.78 43.8884 36.08 43.3364 36.296C42.7924 36.512 42.1964 36.62 41.5484 36.62ZM41.5364 35.252C41.9604 35.252 42.3524 35.18 42.7124 35.036C43.0724 34.892 43.3844 34.688 43.6484 34.424C43.9124 34.152 44.1164 33.84 44.2604 33.488C44.4124 33.128 44.4884 32.732 44.4884 32.3C44.4884 31.868 44.4124 31.476 44.2604 31.124C44.1164 30.764 43.9124 30.452 43.6484 30.188C43.3844 29.916 43.0724 29.708 42.7124 29.564C42.3524 29.42 41.9604 29.348 41.5364 29.348C41.1124 29.348 40.7204 29.42 40.3604 29.564C40.0084 29.708 39.6964 29.916 39.4244 30.188C39.1604 30.452 38.9524 30.764 38.8004 31.124C38.6564 31.476 38.5844 31.868 38.5844 32.3C38.5844 32.724 38.6564 33.116 38.8004 33.476C38.9524 33.836 39.1604 34.152 39.4244 34.424C39.6884 34.688 40.0004 34.892 40.3604 35.036C40.7204 35.18 41.1124 35.252 41.5364 35.252ZM51.7139 36.5V28.1H53.2739V35.18H57.6659V36.5H51.7139ZM64.7839 36.5L61.1119 28.1H62.8039L66.0799 35.696H65.1079L68.4199 28.1H69.9799L66.3199 36.5H64.7839ZM76.3063 31.592H80.4823V32.876H76.3063V31.592ZM76.4263 35.192H81.1663V36.5H74.8663V28.1H80.9983V29.408H76.4263V35.192ZM86.9053 36.5V28.1H90.3613C91.1053 28.1 91.7413 28.22 92.2693 28.46C92.8053 28.7 93.2173 29.044 93.5053 29.492C93.7933 29.94 93.9373 30.472 93.9373 31.088C93.9373 31.704 93.7933 32.236 93.5053 32.684C93.2173 33.124 92.8053 33.464 92.2693 33.704C91.7413 33.936 91.1053 34.052 90.3613 34.052H87.7693L88.4653 33.344V36.5H86.9053ZM92.4013 36.5L90.2773 33.452H91.9453L94.0813 36.5H92.4013ZM88.4653 33.512L87.7693 32.768H90.2893C90.9773 32.768 91.4933 32.62 91.8373 32.324C92.1893 32.028 92.3653 31.616 92.3653 31.088C92.3653 30.552 92.1893 30.14 91.8373 29.852C91.4933 29.564 90.9773 29.42 90.2893 29.42H87.7693L88.4653 28.652V33.512ZM105.811 36.5L109.591 28.1H111.127L114.919 36.5H113.287L110.035 28.928H110.659L107.419 36.5H105.811ZM107.551 34.556L107.971 33.332H112.507L112.927 34.556H107.551ZM133.208 28.1H134.768V36.5H133.208V28.1ZM128.864 36.5H127.304V28.1H128.864V36.5ZM133.328 32.9H128.732V31.568H133.328V32.9ZM144.955 36.62C144.299 36.62 143.695 36.512 143.143 36.296C142.591 36.08 142.111 35.78 141.703 35.396C141.295 35.004 140.979 34.548 140.755 34.028C140.531 33.5 140.419 32.924 140.419 32.3C140.419 31.676 140.531 31.104 140.755 30.584C140.979 30.056 141.295 29.6 141.703 29.216C142.111 28.824 142.591 28.52 143.143 28.304C143.695 28.088 144.295 27.98 144.943 27.98C145.599 27.98 146.199 28.088 146.743 28.304C147.295 28.52 147.775 28.824 148.183 29.216C148.591 29.6 148.907 30.056 149.131 30.584C149.355 31.104 149.467 31.676 149.467 32.3C149.467 32.924 149.355 33.5 149.131 34.028C148.907 34.556 148.591 35.012 148.183 35.396C147.775 35.78 147.295 36.08 146.743 36.296C146.199 36.512 145.603 36.62 144.955 36.62ZM144.943 35.252C145.367 35.252 145.759 35.18 146.119 35.036C146.479 34.892 146.791 34.688 147.055 34.424C147.319 34.152 147.523 33.84 147.667 33.488C147.819 33.128 147.895 32.732 147.895 32.3C147.895 31.868 147.819 31.476 147.667 31.124C147.523 30.764 147.319 30.452 147.055 30.188C146.791 29.916 146.479 29.708 146.119 29.564C145.759 29.42 145.367 29.348 144.943 29.348C144.519 29.348 144.127 29.42 143.767 29.564C143.415 29.708 143.103 29.916 142.831 30.188C142.567 30.452 142.359 30.764 142.207 31.124C142.063 31.476 141.991 31.868 141.991 32.3C141.991 32.724 142.063 33.116 142.207 33.476C142.359 33.836 142.567 34.152 142.831 34.424C143.095 34.688 143.407 34.892 143.767 35.036C144.127 35.18 144.519 35.252 144.943 35.252ZM155.12 36.5V28.1H156.404L160.076 34.232H159.404L163.016 28.1H164.3L164.312 36.5H162.836L162.824 30.416H163.136L160.064 35.54H159.368L156.248 30.416H156.608V36.5H155.12ZM172.021 31.592H176.197V32.876H172.021V31.592ZM172.141 35.192H176.881V36.5H170.581V28.1H176.713V29.408H172.141V35.192Z" fill="#025373"/>
                            <path d="M197 36L193 32L197 28" stroke="#025373" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M193 32H203" stroke="#025373" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                          </svg>
                        </b-button> -->
                        <b-button @click="resetProduct()" class="button-svg">
                          <svg width="182" height="65" viewBox="0 0 182 65" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M0 31C0 13.8792 13.8792 0 31 0H151C168.121 0 182 13.8792 182 31V34C182 51.1208 168.121 65 151 65H31C13.8792 65 0 51.1208 0 34V31Z" fill="#025373"/>
                            <path d="M23.94 37L27.72 28.6H29.256L33.048 37H31.416L28.164 29.428H28.788L25.548 37H23.94ZM25.68 35.056L26.1 33.832H30.636L31.056 35.056H25.68ZM38.1163 37V28.6H41.7883C42.7003 28.6 43.5003 28.776 44.1883 29.128C44.8763 29.48 45.4123 29.968 45.7963 30.592C46.1803 31.216 46.3723 31.952 46.3723 32.8C46.3723 33.64 46.1803 34.376 45.7963 35.008C45.4123 35.632 44.8763 36.12 44.1883 36.472C43.5003 36.824 42.7003 37 41.7883 37H38.1163ZM39.6763 35.68H41.7163C42.3483 35.68 42.8923 35.56 43.3483 35.32C43.8123 35.08 44.1683 34.744 44.4163 34.312C44.6723 33.88 44.8003 33.376 44.8003 32.8C44.8003 32.216 44.6723 31.712 44.4163 31.288C44.1683 30.856 43.8123 30.52 43.3483 30.28C42.8923 30.04 42.3483 29.92 41.7163 29.92H39.6763V35.68ZM52.0303 37V28.6H55.7023C56.6143 28.6 57.4143 28.776 58.1023 29.128C58.7903 29.48 59.3263 29.968 59.7103 30.592C60.0943 31.216 60.2863 31.952 60.2863 32.8C60.2863 33.64 60.0943 34.376 59.7103 35.008C59.3263 35.632 58.7903 36.12 58.1023 36.472C57.4143 36.824 56.6143 37 55.7023 37H52.0303ZM53.5903 35.68H55.6303C56.2623 35.68 56.8063 35.56 57.2623 35.32C57.7263 35.08 58.0823 34.744 58.3303 34.312C58.5863 33.88 58.7143 33.376 58.7143 32.8C58.7143 32.216 58.5863 31.712 58.3303 31.288C58.0823 30.856 57.7263 30.52 57.2623 30.28C56.8063 30.04 56.2623 29.92 55.6303 29.92H53.5903V35.68ZM73.2608 37V28.6H74.5448L79.8128 35.068H79.1768V28.6H80.7248V37H79.4408L74.1728 30.532H74.8088V37H73.2608ZM88.4157 32.092H92.5917V33.376H88.4157V32.092ZM88.5357 35.692H93.2757V37H86.9757V28.6H93.1077V29.908H88.5357V35.692ZM100.878 37L98.0935 28.6H99.7135L102.198 36.196H101.394L103.974 28.6H105.414L107.922 36.196H107.142L109.686 28.6H111.174L108.39 37H106.734L104.442 30.148H104.874L102.546 37H100.878ZM122.749 37L126.529 28.6H128.065L131.857 37H130.225L126.973 29.428H127.597L124.357 37H122.749ZM124.489 35.056L124.909 33.832H129.445L129.865 35.056H124.489ZM136.925 37V28.6H140.381C141.125 28.6 141.761 28.72 142.289 28.96C142.825 29.2 143.237 29.544 143.525 29.992C143.813 30.44 143.957 30.972 143.957 31.588C143.957 32.204 143.813 32.736 143.525 33.184C143.237 33.632 142.825 33.976 142.289 34.216C141.761 34.456 141.125 34.576 140.381 34.576H137.789L138.485 33.844V37H136.925ZM138.485 34.012L137.789 33.256H140.309C140.997 33.256 141.513 33.112 141.857 32.824C142.209 32.528 142.385 32.116 142.385 31.588C142.385 31.052 142.209 30.64 141.857 30.352C141.513 30.064 140.997 29.92 140.309 29.92H137.789L138.485 29.152V34.012ZM149.515 37V28.6H152.971C153.715 28.6 154.351 28.72 154.879 28.96C155.415 29.2 155.827 29.544 156.115 29.992C156.403 30.44 156.547 30.972 156.547 31.588C156.547 32.204 156.403 32.736 156.115 33.184C155.827 33.632 155.415 33.976 154.879 34.216C154.351 34.456 153.715 34.576 152.971 34.576H150.379L151.075 33.844V37H149.515ZM151.075 34.012L150.379 33.256H152.899C153.587 33.256 154.103 33.112 154.447 32.824C154.799 32.528 154.975 32.116 154.975 31.588C154.975 31.052 154.799 30.64 154.447 30.352C154.103 30.064 153.587 29.92 152.899 29.92H150.379L151.075 29.152V34.012Z" fill="#F1F1F1"/>
                          </svg>
                        </b-button>
                      </div>
                    </div>
                </div>
            </div>
        </b-modal>

    </section>
  </template>

<script>

  export default {
    layout: 'header',
    head() {
      return {
        title: 'Add App - ' + this.$config.appName
      }
    },
    data() {
      return {
        nombre: null,
        descripcion: '',
        plan: null,
        vencimiento: '',
        cliente: null,
        sitio: null,
        administrador: null,
        activo: true,
        renovacion: false,
        id: null,
        fechafinal: '',
        isCardModalActive: false
      }
   },
    methods: {
      createProduct () {
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
          this.submit();
        } else {
          console.log("No va, arreglar. Notificando");
          this.$buefy.toast.open({
              message: 'App not added, please check info.',
              type: 'is-danger'
          })
        }
      },
     async submit () {
        console.log("Todo valido, enviando");
        console.log("Sumando renovacion a la fecha");
        if (this.plan == 'anual'){
          var fechaNew = new Date(this.vencimiento);
          var fechaMod = fechaNew.setMonth(fechaNew.getMonth()+12);
          var fechaFormat = new Date(fechaMod);
          this.vencimiento = fechaFormat;
          this.fechafinal = new Intl.DateTimeFormat("en-GB").format(this.vencimiento);
        } else if (this.plan == 'mensual'){
          var fechaNew = new Date(this.vencimiento);
          var fechaMod = fechaNew.setMonth(fechaNew.getMonth()+1);
          var fechaFormat = new Date(fechaMod);
          this.vencimiento = fechaFormat;
          this.fechafinal = new Intl.DateTimeFormat("en-GB").format(this.vencimiento);
        };
        const envio = await this.$axios.$post('/herramienta/', {'nombre': this.nombre, 'descripcion': this.descripcion, 'plan': this.plan, 'vencimiento': this.vencimiento, 'cliente': this.cliente, 'sitio': this.sitio, 'administrador': this.administrador, 'activo': this.activo, 'renovacion': this.renovacion }, {crossdomain: true, headers: {"Content-Type": "application/json", "accept": "application/json"}});
        console.log("Enviado, notificando");
        this.isCardModalActive = true
      },
      async redirect () {
        console.log("Notificado, consiguiendo ID");
        const response = await this.$axios.$get('/herramienta/latest/' + this.nombre);
        console.log("Id servicio:");
        console.log(response.data[0]);
        this.id = response.data[0];
        console.log("Habemus ID, redireccionando a pagina de este");
        this.$router.push('/app/'+ this.id);
      },
      resetProduct () {
        this.nombre = "";
        this.descripcion = "";
        this.plan = "";
        this.vencimento = "";
        this.cliente = "";
        this.sitio = "";
        this.administrador = "";
        this.renovacion = false;
        this.id = null;
        this.isCardModalActive = false;
        this.$router.go();
      }
    }
  }

</script>

<style>
  
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600&display=swap');
  
  
  html, body, button, input, optgroup, select, textarea {
    font-family: 'Montserrat', sans-serif !important;
  }
  select {
    color: #F1F1F1 !important;
    option { 
      color: #F1F1F1 !important;
    }
  }
  html {
    background-color: #1b1b1b !important;
  }

  ::-webkit-scrollbar {
      width: 0px;
      background: transparent; /* make scrollbar transparent */
  }
  ::-moz-scrollbar {
    width: 0px;
      background: transparent; /* make scrollbar transparent */
  }
  .container {
    width: 100% !important;
    max-width: none !important;
  }
  
  .actions {
    padding: 10px 0;
  }
  
  .glyphicon-euro {
    font-size: 12px;
  }
  
  .table{
    width:100%;
  }
  
  .table thead td, .table thead th {
    border-width: 0 0 1px;
    font-size: .85em;
    border-color: #DFDFDF;
    padding-bottom: 1.5%;
  }
  
  .column {
    font-family: 'Montserrat';
    font-style: normal;
    font-weight: 600;
    font-size: 30px;
    line-height: 37px;
    color: #A4A4A4;
    max-width: 75%;
  }
  .select:not(.is-multiple):not(.is-loading)::after {
    border-color: #025373 !important;
  }
  .switch input[type=checkbox]:checked + .check.is-danger {
    background: #025373;
  }
  .switch:hover input[type=checkbox]:checked + .check.is-danger {
    background: #025373;
  }
  .switch input[type=checkbox]:focus:checked + .check.is-danger, .switch input[type=checkbox]:active:checked + .check.is-danger {
    box-shadow: none;
  }

  .filas {
    display: flex;
    flex-direction: column;    
  }
  .fila {
    display: block;
    -ms-flex-preferred-size: 0;
    flex-basis: 0;
    -webkit-box-flex: 1;
    -ms-flex-positive: 1;
    flex-grow: 1;
    -ms-flex-negative: 1;
    flex-shrink: 1;
    padding: 0.75rem;
  }
  .botonsvg:hover .botonsvg-fondo{
    fill: #F1F1F1;
  }
  .botonsvg:hover .botonsvg-icono {
    stroke: #025373;
  }
  .botonsvg:hover .botonsvg-texto {
    fill: #025373;
  }
  .botonsvg2:hover .botonsvg2-icono {
    stroke: #025373;
  }
  .botonsvg2:hover .botonsvg2-texto {
    fill: #025373;
  }
  .botonsvg2:hover .botonsvg2-fondo{
    fill: #F1F1F1;
  }
  .botonsvg2:hover .botonsvg2-icono {
    stroke: #025373;
  }
  .botonsvg2:hover .botonsvg2-texto {
    fill: #025373;
  }
  .botonsvg2:hover .botonsvg2-fondo{
    fill: #F1F1F1;
  }

  h3 {
    font-family: 'Montserrat';
    font-style: normal;
    font-weight: 600;
    font-size: 30px;
    line-height: 37px;
    color: #A4A4A4;
  }
  .help.is-danger {
    color: #E61637;
  }
  .has-text-danger {
    color: #E61637 !important;
  }
  .taginput .is-danger.taginput-container.is-focusable, .is-danger.textarea, .is-danger.input {
    border-color: #E61637 !important;
  }
  .input-texto input {
    border: none;
    box-shadow: none;
    border-bottom: 1px solid;
    border-radius: 0;
    border-color: #DFDFDF;
    color: white;
    height: 55px;
    text-align: left;
    margin: 0px;
    padding-left: calc(0.75em - 5px);
  }
  input {
  color-scheme: dark;
  }
  .input-fecha input {
    color: white;
    width: 100% !important;
    display: block;
  }
  .card {
    background-color: #252525;
  }
  .input-detalles {
    border: none;
    box-shadow: none;
    border-radius: 0;
    color: #F1F1F1;
    text-align: right;
    margin: 0px;
  }
  .select select, .taginput .taginput-container.is-focusable, .textarea, .input {
    color: #F1F1F1;
    background-color: #252525;
  }
  .textarea::placeholder {
    color: #F1F1F1;
  }
  .input {
    background-color: #252525;
    color: #F1F1F1;
  }
  .detalles-filas {
    display: flex;
    flex-direction: column;
  }
  
  .detalles-columas {
    display: flex;
    flex-direction: row;
  }
  .detalles-columa:active {
    border-color: #025373;
  }
  .detalles-columa:focus {
    border-color: #025373;
  }
  .detalles-columa:target {
    border-color: #025373;
  }
  .detalles-columa:nth-of-type(2):hover{
    border-color: #b5b5b5;
  }
  .button-svg {
    background: none;
    color: inherit;
    border: none;
    padding: 0;
    font: inherit;
    cursor: pointer;
    outline: inherit;
}
  .detalles-columa {
    font-weight: 400;
    font-size: 1rem;
    color: #A4A4A4;
    margin: 0;
    padding: 0;
    width: 100%;
    border-bottom: 1px solid;
    border-radius: 0;
    border-color: #DFDFDF;
    padding-top: 1rem;
    padding-bottom: 1rem;
  }
  .detalles-columa:first-child {
    width: 45%;
  }
  #campocorto {
    width: 60%;
  }

  .input-texto input:active {
    border: none !important;
    box-shadow: none !important;
    -webkit-box-shadow:none !important;
  }
  
  .input-texto input::placeholder {
    color: #A4A4A4;
  }
  .input-detalles input:active {
    border: none !important;
    box-shadow: none !important;
    -webkit-box-shadow:none !important;
  }
  
  .input-detalles input::placeholder {
    color: #A4A4A4;
  }  
  .rows {
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: flex-start;
  }
  
  .b-radio ,radio {
    font-size: 20px !important;
    font-weight: 400;
  }
  
   .b-checkbox ,checkbox {
    font-size: 20px !important;
    font-weight: 400;
  }
  
  .field label {
    font-weight: 400;
    color: #A4A4A4;
    margin-bottom: 1em;
  }
  
  .label:not(:last-child) {
    margin-bottom: 1em;
  }

  .field-body{
    margin-left: 0.5em;
  }
  
  .b-radio.radio:not(.button) {
    margin-right: 5em;
  }
  
  .field:not(:last-child) {
    margin-bottom: 0;
  }
  
  .b-checkbox.checkbox:not(.button) {
    margin-left: 0.75em;
  }
  
  .b-radio.radio:hover input[type=radio]:not(:disabled) + .check {
    border-color: #025373;
  }
  
  .b-radio.radio input[type=radio]:checked + .check {
    border-color: #025373;
  }
  
  .b-radio.radio input[type=radio] + .check:before {
    background-color: #025373;
  }
  .b-radio.radio input[type=radio]:focus:checked + .check {
    box-shadow: none;
  }
  .b-radio.radio input[type=radio]:focus + .check {
    box-shadow: none;
  }
  .b-checkbox.checkbox:hover input[type=checkbox]:not(:disabled) + .check {
    border-color: #025373;
  }
  .b-checkbox.checkbox input[type=checkbox]:focus:checked + .check {
    box-shadow: none;
  }
  .b-checkbox.checkbox input[type=checkbox]:checked + .check {
    border-color: #025373;
    background: #025373 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1 1'%3E%3Cpath style='fill:%23fff' d='M 0.04038059,0.6267767 0.14644661,0.52071068 0.42928932,0.80355339 0.3232233,0.90961941 z M 0.21715729,0.80355339 0.85355339,0.16715729 0.95961941,0.2732233 0.3232233,0.90961941 z'%3E%3C/path%3E%3C/svg%3E") no-repeat center center;
  }
  .select select:focus, .taginput .taginput-container.is-focusable:focus, .textarea:focus, .input:focus, .select select.is-focused, .taginput .is-focused.taginput-container.is-focusable, .is-focused.textarea, .is-focused.input, .select select:active, .taginput .taginput-container.is-focusable:active, .textarea:active, .input:active, .select select.is-active, .taginput .is-active.taginput-container.is-focusable, .is-active.textarea, .is-active.input {
    border-color: #025373;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
  .help.is-danger {
    visibility: hidden;
    line-height: 1em;
  }
  .help.is-danger:after {
      content: 'Check this field.';
      visibility: visible;
      display: block;
  }
  .control .help.counter {
    visibility: visible !important;
  }
  .textarea:not([rows]) {
    min-height: 4em;
    max-height: 10em;
  }
</style>
