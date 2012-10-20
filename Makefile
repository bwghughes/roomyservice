ci:
	sniffer . -x --with-growl -x --with-coverage -x --cover-package=pintapp.models,pintapp.app -x --cover-html

deploy:
	dotcloud push roomyapp

test:
	nosetests --with-coverage -x --cover-package=pintapp.models,pintnapp.app -x --cover-html

doc:
	echo "Docs"
