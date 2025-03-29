if status is-interactive
    # Commands to run in interactive sessions can go here
    switch (uname -s)
        case Darwin
            /opt/homebrew/bin/brew shellenv | source
    	# do things for macOS
        case Linux
            /home/linuxbrew/.linuxbrew/Homebrew/bin/brew shellenv | source
    	# do things for Linux
        case '*'
    	# do things for other OSs
    end

    set --export --global GOPATH $HOME/go

    starship init fish | source
    fnm env --use-on-cd --shell fish | source
end

