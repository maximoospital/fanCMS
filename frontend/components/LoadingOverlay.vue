<template>
    <div class="container">
        <div id="overlay">
            <div class="overlay__inner">
                <div class="overlay__content">
                    <svg width="235" height="33" viewBox="0 0 463 94" class="logofade" xmlns="http://www.w3.org/2000/svg" shape-rendering="auto">
                    <path d="M6.39999 91.4V36.32H0.519989V24.92H6.39999V21.92C6.39999 9.2 15.4 2.60001 27.76 2.60001H30.52V14C22.36 14 18.88 16.88 18.88 21.8V24.92H30.52V36.32H18.88V91.4H6.39999Z" fill="#025373"/>
                    <path d="M91.48 91.4V81.08H91.24C86.56 89 78.16 93.08 68.68 93.08C49.24 93.08 33.4 78.44 33.4 59.24C33.4 38 48.64 23.12 68.2 23.12C77.92 23.12 86.08 26.72 91.24 34.28H91.48V24.92H103.96V91.4H91.48ZM91.72 58.28C91.72 45.32 82.36 34.52 68.56 34.52C56.08 34.52 45.88 45.2 45.88 58.28C45.88 71.36 56.08 81.68 68.56 81.68C81.04 81.68 91.72 70.88 91.72 58.28Z" fill="#025373"/>
                    <path d="M166.48 91.4V55.16C166.48 41.12 160.96 34.52 149.92 34.52C138.88 34.52 132.4 42.56 132.4 55.04V91.4H119.92V24.92H131.56V32H131.8C136.72 25.64 143.56 23.12 151.24 23.12C167.2 23.12 178.96 33.2 178.96 51.56V91.4H166.48Z" fill="#025373"/>
                    <path d="M259.24 36.32C255.4 26.6 247 20.84 237.76 20.84C223.6 20.84 214 32.96 214 46.76C214 60.56 223.84 73.16 237.88 73.16C246.88 73.16 254.56 68.12 259.24 58.16H283C277.48 79.52 259.12 93.08 238.12 93.08C225.76 93.08 214.12 88.76 205 79.76C195.4 70.4 191.32 59.12 191.32 45.68C191.32 22.16 211.6 0.920013 237.04 0.920013C249.28 0.920013 259.12 4.28001 268 11.84C276.4 19.04 281.44 27.2 283 36.32H259.24Z" fill="#f1f1f1"/>
                    <path d="M367.59 91.4L368.31 24.92L368.07 24.68L349.11 91.4H334.11L314.91 24.08L315.63 91.4H294.75V2.60001H323.91L341.55 61.04H341.79L359.19 2.60001H388.47V91.4H367.59Z" fill="#f1f1f1"/>
                    <path d="M439.35 28.52C438.39 22.16 435.75 19.88 431.31 19.88C427.11 19.88 423.51 22.88 423.51 26.84C423.51 32.12 428.31 34.52 438.03 38.72C457.59 47.12 462.51 54.2 462.51 65.84C462.51 83 450.75 93.08 431.55 93.08C412.35 93.08 399.51 83 399.51 63.92V62H422.07C422.19 69.32 425.79 74.12 431.43 74.12C436.11 74.12 439.95 70.4 439.95 65.6C439.95 58.52 430.11 55.4 422.07 52.16C407.55 46.28 400.95 38.6 400.95 27.08C400.95 11.96 415.59 0.920013 431.91 0.920013C437.79 0.920013 442.95 2.24001 447.63 4.64001C457.11 9.56001 461.67 16.64 461.79 28.52H439.35Z" fill="#f1f1f1"/>
                    </svg>
                    <br>
                    <span class="spinner"></span>
                </div>
            </div>
        </div>
        <no-ssr>
            <script>
            document.onreadystatechange = () => {
                if (document.readyState === 'complete') {
                var x = document.getElementById("overlay");
                x.style.opacity = 0;
                setTimeout(function() {
                    x.style.display = "none";
                }, 650);
                }
            };
            </script>
        </no-ssr>      
    </div>
</template>
<script>
  export default {
    name: 'LoadingOverlay',
  }
</script>