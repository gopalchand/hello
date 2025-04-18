Procedure:

# 1. Initialize Git (if not already done)
git init

# 2. Add the remote origin (replace with your actual username!)
git remote add origin https://github.com/yourusername/hello_cmake.git

# 3. Add and commit your files
git add .
git commit -m "Initial commit with CMake Python extension"

# 4. Change email to noreply email using https://www.github.com/emails for details
git config --global user.email "12345678+yourusername@users.noreply.github.com"
git commit --amend --reset-author

# 5. Push to GitHub
git branch -M main
git push -f origin main
