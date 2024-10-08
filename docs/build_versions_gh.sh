#!/bin/bash

# Automatically detect all versions in the docs/source/versions/ directory
VERSIONS=($(ls -d docs/source/versions/* | xargs -n 1 basename | sort -r))

# Display a message before starting the build process
echo "========================================="
echo "Building docs for versions: ${VERSIONS[@]}"
echo "========================================="

# Build each version
for version in "${VERSIONS[@]}"; do
  echo "Building version: $version"
  
  # Set the CURRENT_VERSION environment variable for this version
  export CURRENT_VERSION=$version
  
  # Run sphinx-build with the root conf.py, specifying the source and build directories
  sphinx-build -b html "docs/source/versions/$version" "docs/build/versions/$version" -c "docs/source"
  
  if [ $? -eq 0 ]; then
    echo "Successfully built: $version"
  else
    echo "Error building version: $version"
    exit 1
  fi
done

# Path to the build directory
BUILD_DIR="docs/build"

# Get the latest version (first item in the array)
LATEST_VERSION=${VERSIONS[0]}

# Automatically detect the repository name from the Git configuration
REPO_URL=$(git config --get remote.origin.url)
REPO_NAME=$(basename -s .git "$REPO_URL")  # Extract only the repository name

# Create the index.html file with a redirect to the latest version
INDEX_FILE="${BUILD_DIR}/index.html"

cat <<EOL > $INDEX_FILE
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="refresh" content="0; url=https://hms-iac.github.io/$REPO_NAME/versions/$LATEST_VERSION/index.html">
    <title>Documentation Redirect</title>
</head>
<body>
    <p>If not redirected, <a href="https://hms-iac.github.io/$REPO_NAME/versions/$LATEST_VERSION/index.html">click here</a>.</p>
</body>
</html>
EOL

echo "========================================="
echo "All versions built successfully."
echo "Website entry point will be: https://hms-iac.github.io/$REPO_NAME/versions/$LATEST_VERSION/index.html"
echo "========================================="
