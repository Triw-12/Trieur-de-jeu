$(function () {
	// Initialisation du slider pour le nombre de joueurs
	const minPlayers = 1;  // Valeur minimale du slider
	const maxPlayers = 20; // Valeur maximale du slider

	$("#players-slider").slider({
	    range: true,
	    min: minPlayers,
	    max: maxPlayers,
	    values: [minPlayers, maxPlayers],
	    slide: function (event, ui) {
		   // Mise à jour des champs min-players et max-players
		   $("#id-min-players").val(ui.values[0]);
		   $("#id-max-players").val(ui.values[1]);
	    }
	});

	// Initialisation des valeurs des champs à celles du slider
	$("#id-min-players").val($("#players-slider").slider("values", 0));
	$("#id-max-players").val($("#players-slider").slider("values", 1));
});

 $(function () {
	// Initialisation du slider pour le nombre de joueurs
	const minTime = 0;  // Valeur minimale du slider
	const maxTime = 360; // Valeur maximale du slider

	$("#time-slider").slider({
	    range: true,
	    min: minTime,
	    max: maxTime,
	    values: [minTime, maxTime],
	    slide: function (event, ui) {
		   // Mise à jour des champs min-players et max-players
		   $("#id-min-time").val(ui.values[0]);
		   $("#id-max-time").val(ui.values[1]);
	    }
	});

	// Initialisation des valeurs des champs à celles du slider
	$("#id-min-time").val($("#time-slider").slider("values", 0));
	$("#id-max-time").val($("#time-slider").slider("values", 1));
});