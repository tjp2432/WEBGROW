/* Radio Grow: radios por género (API pública Radio Browser, sin claves). */
(function () {
    var API = 'https://de1.api.radio-browser.info/json/stations/search';
    var fab = document.getElementById('radioFab');
    var widget = document.getElementById('radioWidget');
    var closeBtn = document.getElementById('radioClose');
    var genres = document.getElementById('radioGenres');
    var now = document.getElementById('radioNow');
    var audio = document.getElementById('radioAudio');
    var playBtn = document.getElementById('radioPlay');
    var prevBtn = document.getElementById('radioPrev');
    var nextBtn = document.getElementById('radioNext');
    var vol = document.getElementById('radioVol');
    if (!fab || !widget) return;

    var stations = [];
    var idx = 0;
    var cache = {};

    fab.addEventListener('click', function () {
        widget.hidden = !widget.hidden;
    });
    closeBtn.addEventListener('click', function () {
        audio.pause();
        setPlayIcon(false);
        widget.hidden = true;
    });

    function setPlayIcon(playing) {
        playBtn.innerHTML = playing
            ? '<i class="bi bi-pause-fill"></i>'
            : '<i class="bi bi-play-fill"></i>';
        fab.classList.toggle('playing', playing);
    }

    function playStation(i) {
        if (!stations.length) return;
        idx = (i + stations.length) % stations.length;
        var s = stations[idx];
        audio.src = s.url_resolved;
        audio.play().then(function () {
            setPlayIcon(true);
        }).catch(function () {
            now.textContent = 'No se pudo reproducir, probá otra';
            setPlayIcon(false);
        });
        now.textContent = s.name || 'Radio en vivo';
    }

    genres.addEventListener('click', function (e) {
        var btn = e.target.closest('button[data-tag]');
        if (!btn) return;
        var tag = btn.getAttribute('data-tag');
        var country = btn.getAttribute('data-country') || '';
        var key = tag + '|' + country;
        Array.prototype.forEach.call(genres.children, function (b) {
            b.classList.toggle('active', b === btn);
        });
        if (cache[key]) {
            stations = cache[key];
            playStation(0);
            return;
        }
        now.textContent = 'Buscando radios...';
        var url = API + '?hidebroken=true&order=votes&reverse=true&limit=20&tag=' + encodeURIComponent(tag);
        if (country) url += '&country=' + encodeURIComponent(country);
        fetch(url)
            .then(function (r) { return r.json(); })
            .then(function (list) {
                stations = (list || []).filter(function (s) {
                    return s.url_resolved && s.url_resolved.indexOf('https://') === 0;
                });
                cache[key] = stations;
                if (!stations.length) {
                    now.textContent = 'Sin radios HTTPS, probá otro género';
                    return;
                }
                playStation(0);
            })
            .catch(function () {
                now.textContent = 'Sin conexión, reintentá';
            });
    });

    playBtn.addEventListener('click', function () {
        if (!audio.src) {
            var first = genres.querySelector('button');
            if (first) first.click();
            return;
        }
        if (audio.paused) {
            audio.play();
            setPlayIcon(true);
        } else {
            audio.pause();
            setPlayIcon(false);
        }
    });
    nextBtn.addEventListener('click', function () { playStation(idx + 1); });
    prevBtn.addEventListener('click', function () { playStation(idx - 1); });
    vol.addEventListener('input', function () { audio.volume = vol.value / 100; });
    audio.volume = 0.8;
    audio.addEventListener('error', function () {
        if (audio.src) playStation(idx + 1);
    });
})();
