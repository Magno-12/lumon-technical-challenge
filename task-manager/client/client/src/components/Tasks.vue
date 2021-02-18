<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Task</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.task-modal>Add Task</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Description</th>
              <th scope="col">Priority</th>
              <th scope="col">Author</th>
              <th scope="col">Worker</th>
              <th scope="col">Completed?</th>
              <th scope="col">Tags</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(task, index) in tasks" :key="index">
              <td>{{ task.title }}</td>
              <td>{{ task.description }}</td>
              <td>{{ task.priority }}</td>
              <td>{{ task.author }}</td>
              <td>{{ task.worker }}</td>
              <td>
                <span v-if="task.completed">Yes</span>
                <span v-else>No</span>
              </td>
              <td>{{ task.tags }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.task-update-modal
                          @click="editTask(task)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteTask(task)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addTaskModal"
            id="task-modal"
            title="Add a new task"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addTaskForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addTaskForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
                  <b-form-group id="form-description-group"
                      label="Description:"
                      label-for="form-description-input">
            <b-form-input id="form-description-input"
                          type="text"
                          v-model="addTaskForm.description"
                          required
                          placeholder="Enter description">
            </b-form-input>
          </b-form-group>
                  <b-form-group id="form-priority-group"
                      label="Priority:"
                      label-for="form-priority-input">
            <b-form-input id="form-priority-input"
                          type="text"
                          v-model="addTaskForm.priority"
                          required
                          placeholder="Enter priority">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-tags-group"
                      label="Tags:"
                      label-for="form-tags-input">
            <b-form-input id="form-tags-input"
                          type="text"
                          v-model="addTaskForm.tags"
                          required
                          placeholder="Enter tags split by ','">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addTaskForm.completed" id="form-checks">
            <b-form-checkbox value="true">Completed?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editTaskModal"
            id="task-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-description-edit-group"
                      label="Description:"
                      label-for="form-description-edit-input">
            <b-form-input id="form-description-edit-input"
                          type="text"
                          v-model="editForm.description"
                          required
                          placeholder="Enter description">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-priority-edit-group"
                      label="Priority:"
                      label-for="form-priority-edit-input">
            <b-form-input id="form-priority-edit-input"
                          type="text"
                          v-model="editForm.priority"
                          required
                          placeholder="Enter priority">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-tags-edit-group"
                      label="Tags:"
                      label-for="form-tags-edit-input">
            <b-form-input id="form-tags-edit-input"
                          type="text"
                          v-model="editForm.tags"
                          required
                          placeholder="Enter tags">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-worker-edit-group"
                      label="Worker:"
                      label-for="form-worker-edit-input">
            <b-form-input id="form-worker-edit-input"
                          type="text"
                          v-model="editForm.worker"
                          required
                          placeholder="Enter worker name">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-completed-edit-group">
          <b-form-checkbox-group v-model="editForm.completed" id="form-checks">
            <b-form-checkbox value="true">Completed?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      tasks: [],
      addTaskForm: {
        title: '',
        author: '',
        completed: [],
        description: '',
        priority: '',
        tags: '',
        worker: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        author: '',
        completed: [],
        description: '',
        priority: '',
        tags: '',
        worker: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTask(payload) {
      const path = 'http://localhost:5000/tasks';
      axios.post(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'Task added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTasks();
        });
    },
    initForm() {
      this.addTaskForm.title = '';
      this.addTaskForm.author = '';
      this.addTaskForm.priority = '';
      this.addTaskForm.description = '';
      this.addTaskForm.tags = '';
      this.addTaskForm.worker = '';
      this.addTaskForm.completed = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.priority = '';
      this.editForm.description = '';
      this.editForm.tags = '';
      this.editForm.worker = '';
      this.editForm.completed = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      let completed = false;
      if (this.addTaskForm.completed[0]) completed = true;
      const payload = {
        title: this.addTaskForm.title,
        author: this.addTaskForm.author,
        priority: this.addTaskForm.priority,
        description: this.addTaskForm.description,
        tags: this.addTaskForm.tags,
        worker: this.addTaskForm.worker,
        completed, // property shorthand
      };
      this.addTask(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      this.initForm();
    },
    editTask(task) {
      this.editForm = task;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTaskModal.hide();
      let completed = false;
      if (this.editForm.completed[0]) completed = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        priority: this.editForm.priority,
        description: this.editForm.description,
        tags: this.editForm.tags,
        worker: this.editForm.worker,
        completed,
      };
      this.updateTask(payload, this.editForm.id);
    },
    updateTask(payload, taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios.put(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'Task updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTaskModal.hide();
      this.initForm();
      this.getTasks(); // why?
    },
    removeTask(taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios.delete(path)
        .then(() => {
          this.getTasks();
          this.message = 'Task removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },
    onDeleteTask(task) {
      this.removeTask(task.id);
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
