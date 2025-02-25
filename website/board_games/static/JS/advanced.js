$(function () {
    function initSlider(sliderId, minField, maxField, minValue, maxValue, step = 1) {
        $(sliderId).slider({
            range: true,
            min: minValue,
            max: maxValue,
            values: [minValue, maxValue],
            step: step,
            slide: function (event, ui) {
                $(minField).val(ui.values[0]);
                $(maxField).val(ui.values[1]);
            }
        });

        // Initialisation des champs avec les valeurs du slider
        $(minField).val($(sliderId).slider("values", 0));
        $(maxField).val($(sliderId).slider("values", 1));
    }

    // Initialiser les sliders
    initSlider("#players-slider", "#id-min-players", "#id-max-players", 1, 20);
    initSlider("#time-slider", "#id-min-time", "#id-max-time", 0, 360, 5);
});

$(document).ready(function () {
    let selectedTags = new Set(); // Stocke les tags sélectionnés
    let showAll = false; // Indique si on est en mode large (true) ou réduit (false)

    // Masquer les tags supplémentaires au démarrage
    $(".hidden-tag").hide();

    // Gestion de la sélection des tags
    $(".tag-btn").click(function () {
        let tagId = $(this).data("tag");

        if (selectedTags.has(tagId)) {
            selectedTags.delete(tagId);
            $(this).removeClass("btn-primary").addClass("btn-outline-primary");
        } else {
            selectedTags.add(tagId);
            $(this).removeClass("btn-outline-primary").addClass("btn-primary");
        }

        $("#id-tags").val(Array.from(selectedTags).join(","));
    });

    // Fonction pour afficher les tags en fonction du mode actuel
    function updateTagDisplay() {
        let searchValue = $("#tag-search").val().toLowerCase();
        let matchingTags = [];

        // Filtrer les tags selon la recherche
        $(".tag-btn").each(function () {
            let tagText = $(this).text().toLowerCase();
            if (tagText.includes(searchValue)) {
                matchingTags.push(this);
            } else {
                $(this).hide();
            }
        });

        // Affichage selon le mode actuel
        $(".tag-btn").hide(); // On cache tous les tags avant d'afficher les bons

        if (showAll) {
            // Mode large → afficher tous les tags correspondant à la recherche
            matchingTags.forEach(tag => $(tag).show());
            $("#show-more-tags").hide();
            $("#show-less-tags").toggle(matchingTags.length > 5);
        } else {
            // Mode réduit → afficher seulement 5 résultats max
            matchingTags.slice(0, 5).forEach(tag => $(tag).show());
            $("#show-more-tags").toggle(matchingTags.length > 5);
            $("#show-less-tags").hide();
        }
    }

    // Recherche dynamique des tags
    $("#tag-search").on("input", function () {
        updateTagDisplay();
    });

    // Affichage des tags cachés → Passe en mode large
    $("#show-more-tags").click(function () {
        showAll = true;
        $(".tag-btn").show(); // Afficher tous les tags d'abord
        updateTagDisplay(); // Ensuite appliquer la recherche
        $(this).hide();
        $("#show-less-tags").show();
    });

    // Repli des tags → Passe en mode réduit
    $("#show-less-tags").click(function () {
        showAll = false;
        updateTagDisplay(); // Appliquer la recherche d'abord, puis réduire à 5
        $(this).hide();
        $("#show-more-tags").show();
    });
});

$(function () {
    $("#age-slider").slider({
        range: "min",
        min: 0,
        max: 14,
        value: 6,  // Valeur par défaut
        step: 1,
        slide: function (event, ui) {
            $("#age-value").text(ui.value);
            $("#age-input").val(ui.value);
        }
    });

    // Initialiser la valeur affichée
    $("#age-value").text($("#age-slider").slider("value"));
});

$(document).ready(function () {
    $("#reset-button").click(function () {
        // Réinitialiser les champs texte
        $("#id-game-name").val("");

        // Réinitialiser les sliders
        $("#players-slider").slider("values", [1, 20]);
        $("#id-min-players").val(1);
        $("#id-max-players").val(20);

        $("#time-slider").slider("values", [0, 360]);
        $("#id-min-time").val(0);
        $("#id-max-time").val(360);

        $("#age-slider").slider("value", 6);
        $("#age-value").text(6);
        $("#age-input").val(6);

        // Réinitialiser les tags sélectionnés
        $(".tag-btn").removeClass("btn-primary").addClass("btn-outline-primary");
        $("#id-tags").val("");

        // Réinitialiser la barre de recherche de tags
        $("#tag-search").val("");

        // Revenir en mode réduit pour les tags
        $(".tag-btn").hide(); // Cacher tous les tags
        $(".tag-btn:lt(5)").show(); // Afficher seulement les 5 premiers
        $("#show-more-tags").show();
        $("#show-less-tags").hide();
    });
});
