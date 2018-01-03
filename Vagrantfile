Vagrant.configure(2) do |config|
    config.vm.box = 'centos/7'
    config.vm.hostname = 'ansible'
    config.vm.network 'private_network',ip: '192.168.2.6'
    config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
    config.vm.network "forwarded_port", guest: 3000, host: 3000
    config.vm.network "forwarded_port", guest: 27017, host: 27017

    config.vm.provider 'virtualbox' do |vb|
      vb.customize ['modifyvm', :id, '--memory', '2048']
    end

    config.vm.provision :ansible_local do |ansible|
      ansible.playbook = 'nodejs-development.yml'
      ansible.galaxy_role_file = 'nodejs-development-requirements.yml'
    end

    config.vm.provision :docker do |d|
    #   d.pull_images "mongo"
      d.run "mongo",
        daemonize: true
    end
  end
