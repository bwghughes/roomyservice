ci:
	sniffer . -x --with-growl -x --with-coverage -x --cover-package=roomyapp -x --cover-html

deploy:
	dotcloud push roomyapp

test:
	nosetests --with-coverage -x --cover-package=roomyapp -x --cover-html

doc:
	echo "Docs"
