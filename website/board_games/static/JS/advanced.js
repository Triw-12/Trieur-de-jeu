$(function () {
    // Initialise un slider en se basant sur la valeur présente dans le champ,
    // sinon utilise la valeur par défaut passée en paramètre.
    function initSlider(sliderId, minField, maxField, minDefault, maxDefault, step = 1) {
        // On récupère les valeurs présentes dans le formulaire (si POST), sinon on utilise le défaut
        const minVal = parseInt($(minField).val()) || minDefault;
        const maxVal = parseInt($(maxField).val()) || maxDefault;

        $(sliderId).slider({
            range: true,
            min: minDefault,
            max: maxDefault,
            values: [minVal, maxVal],
            step: step,
            slide: function (_, ui) {
                $(minField).val(ui.values[0]);
                $(maxField).val(ui.values[1]);
            }
        });
    }

    // Met à jour l'affichage des tags en fonction de la recherche
    function updateTagDisplay() {
        let searchValue = $("#tag-search").val().toLowerCase();
        let matchingTags = $(".tag-btn").filter(function () {
            return $(this).text().toLowerCase().includes(searchValue);
        });
        $(".tag-btn").hide();
        matchingTags.slice(0, showAll ? matchingTags.length : 5).show();
        $("#show-more-tags").toggle(matchingTags.length > 5 && !showAll);
        $("#show-less-tags").toggle(showAll);
    }

    // Initialisation des tags déjà sélectionnés (issus du formulaire POST ou vides pour un GET)
    let selectedTags = new Set($("#id-tags").val()?.split(",").filter(Boolean));
    let showAll = false;
    $(".hidden-tag").hide();

    // Mise à jour de l'apparence des boutons tags selon la sélection
    selectedTags.forEach(tag => {
        $(".tag-btn[data-tag='" + tag + "']").removeClass("btn-outline-primary").addClass("btn-primary");
    });

    // Gestion du clic sur un tag
    $(".tag-btn").click(function () {
        let tagId = $(this).data("tag");
        if (selectedTags.has(tagId)) {
            selectedTags.delete(tagId);
        } else {
            selectedTags.add(tagId);
        }
        $(this).toggleClass("btn-primary btn-outline-primary");
        $("#id-tags").val(Array.from(selectedTags).join(","));
    });

    $("#tag-search").on("input", updateTagDisplay);
    $("#show-more-tags").click(() => { showAll = true; updateTagDisplay(); });
    $("#show-less-tags").click(() => { showAll = false; updateTagDisplay(); });

    // Initialisation du slider pour l'âge
    // Si le champ #age-input est vide (GET) on utilise la valeur par défaut 6, sinon on prend la valeur envoyée par POST.
    const ageVal = parseInt($("#age-input").val()) || 6;
    $("#age-slider").slider({
        range: "min",
        min: 0,
        max: 14,
        value: ageVal,
        step: 1,
        slide: function (_, ui) {
            $("#age-value").text(ui.value);
            $("#age-input").val(ui.value);
        }
    });
    $("#age-value").text(ageVal);

    // Initialisation des sliders pour le nombre de joueurs et la durée,
    // en utilisant la valeur déjà présente dans le formulaire ou la valeur par défaut.
    initSlider("#players-slider", "#id-min-players", "#id-max-players", 1, 20);
    initSlider("#time-slider", "#id-min-time", "#id-max-time", 0, 360, 5);

    updateTagDisplay();

    // Bouton de réinitialisation qui remet les valeurs par défaut dans le formulaire.
    // Ici, la réinitialisation se fait localement (pas de stockage persistant).
    $("#reset-button").click(function () {
        // Réinitialisation des champs de texte et select
        $("#id-game-name").val("");
        $("#sort_by").val("name");

        // Réinitialisation du slider des joueurs
        $("#players-slider").slider("values", [1, 20]);
        $("#id-min-players").val(1);
        $("#id-max-players").val(20);

        // Réinitialisation du slider de la durée
        $("#time-slider").slider("values", [0, 360]);
        $("#id-min-time").val(0);
        $("#id-max-time").val(360);

        // Réinitialisation du slider de l'âge
        $("#age-slider").slider("value", 6);
        $("#age-value").text(6);
        $("#age-input").val(6);

        // Réinitialisation des tags
        $(".tag-btn").removeClass("btn-primary").addClass("btn-outline-primary");
        selectedTags.clear();
        $("#id-tags").val("");
        $("#tag-search").val("");
        showAll = false;
        updateTagDisplay();
    });
});
