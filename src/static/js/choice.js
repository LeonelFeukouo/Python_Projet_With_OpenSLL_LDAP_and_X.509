
new TomSelect('#select-repo',{
		valueField: 'pseudo',
		labelField: 'pseudo',
		searchField: 'pseudo',
		// fetch remote data
		load: function(query, callback) {

			var url = 'https://127.0.0.1:5000/search/' + encodeURIComponent(query);
			fetch(url)
				.then(response => response.json())
				.then(json => {
					callback(json.items);
				}).catch(()=>{
					callback();
				});

		},
		// custom rendering functions for options and items
		render: {
			option: function(item, escape) {
				return `<div class="py-2 d-flex">
							<div class="icon me-3">
								<img class="img-fluid" src="${item.pseudo}" />
							</div>
							<div>
								<div class="mb-1">
									<span class="h4">
										${ escape(item.pseudo) }
									</span>
									<span class="text-muted">by ${ escape(item.pseudo) }</span>
								</div>
						 		<div class="description">${ escape(item.pseudo) }</div>
							</div>
						</div>`;
			},
			item: function(item, escape) {
				return `<div class="py-2 d-flex">
							<div class="icon me-3">
								<img class="img-fluid" src="${item.pseudo}" />
							</div>
							<div>
								<div class="mb-1">
									<span class="h4">
										${ escape(item.pseudo) }
									</span>
									<span class="text-muted">by ${ escape(item.pseudo) }</span>
								</div>
						 		<div class="description">${ escape(item.pseudo) }</div>
							</div>
						</div>`;
			}
		},
	});
