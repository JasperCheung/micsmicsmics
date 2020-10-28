deploy-backend-staging:
	git subtree push --prefix server backend-staging master

deploy-backend-prod:
	git subtree push --prefix server backend-prod master

deploy-backend:
	git subtree push --prefix server backend-staging master
	git subtree push --prefix server backend-prod master
